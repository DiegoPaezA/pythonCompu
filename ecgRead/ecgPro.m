ecg = csvread('C:\Users\diegopaez\PycharmProjects\ecgRead\ecgRaw_250Hz.txt',0);

%   Remove lower frequencies
    fresult=fft(ecg);
    fresult(1 : round(length(fresult)*5/samplingrate))=0;
    fresult(end - round(length(fresult)*5/samplingrate) : end)=0;
    corrected=real(ifft(fresult));
    %   Filter - first pass
    WinSize = floor(samplingrate * 571 / 1000);
    if rem(WinSize,2)==0
        WinSize = WinSize+1;
    end
    filtered1=ecgdemowinmax(corrected, WinSize);
    %   Scale ecg
    peaks1=filtered1/(max(filtered1)/7);
    %   Filter by threshold filter
    for data = 1:1:length(peaks1)
        if peaks1(data) < 4
            peaks1(data) = 0;
        else
            peaks1(data)=1;
        end
    end
    positions=find(peaks1);
    distance=positions(2)-positions(1);
    for data=1:1:length(positions)-1
        if positions(data+1)-positions(data)<distance
            distance=positions(data+1)-positions(data);
        end
    end
    % Optimize filter window size
    QRdistance=floor(0.04*samplingrate);
    if rem(QRdistance,2)==0
        QRdistance=QRdistance+1;
    end
    WinSize=2*distance-QRdistance;
    % Filter - second pass
    filtered2=ecgdemowinmax(corrected, WinSize);
    peaks2=filtered2;
    for data=1:1:length(peaks2)
        if peaks2(data)<4
            peaks2(data)=0;
        else
            peaks2(data)=1;
        end
    end
    %   Create figure - stages of processing
    figure(demo); set(demo, 'Name', strcat(plotname, ' - Processing Stages'));
    %   Original input ECG data
    subplot(3, 2, 1); plot((ecg-min(ecg))/(max(ecg)-min(ecg)));
    title('\bf1. Original ECG'); ylim([-0.2 1.2]);
    %   ECG with removed low-frequency component
    subplot(3, 2, 2); plot((corrected-min(corrected))/(max(corrected)-min(corrected)));
    title('\bf2. FFT Filtered ECG'); ylim([-0.2 1.2]);
    %   Filtered ECG (1-st pass) - filter has default window size
    subplot(3, 2, 3); stem((filtered1-min(filtered1))/(max(filtered1)-min(filtered1)));
    title('\bf3. Filtered ECG - 1^{st} Pass'); ylim([0 1.4]);
    %   Detected peaks in filtered ECG
    subplot(3, 2, 4); stem(peaks1);
    title('\bf4. Detected Peaks'); ylim([0 1.4]);
    %   Filtered ECG (2-d pass) - now filter has optimized window size
    subplot(3, 2, 5); stem((filtered2-min(filtered2))/(max(filtered2)-min(filtered2)));
    title('\bf5. Filtered ECG - 2^d Pass'); ylim([0 1.4]);
    %   Detected peaks - final result
    subplot(3, 2, 6); stem(peaks2);
    title('\bf6. Detected Peaks - Finally'); ylim([0 1.4]);
    %   Create figure - result
    figure(demo+1); set(demo+1, 'Name', strcat(plotname, ' - Result'));
    %   Plotting ECG in green
    plot((ecg-min(ecg))/(max(ecg)-min(ecg)), '-g'); title('\bf Comparative ECG R-Peak Detection Plot');
    %   Show peaks in the same picture
    hold on
    %   Stemming peaks in dashed black
    stem(peaks2'*((ecg-min(ecg))/(max(ecg)-min(ecg)))', ':k');
    %   Hold off the figure
    hold off
% ecgRaw = corrected;
% 
% Fs = 250;                         % frecuencia de muestreo
% Vt = 0:1/Fs:(length(ecgRaw(:,1))-1)/Fs;  % 0 - 60 segundos, pasos de 1/240hz tasa de muestreo
% N = length(ecgRaw);
% duration_in_seconds = N/Fs;
% Vt=Vt';
% 
% 
% %Filtro
% % Desenho do filtro passa-baixa
% Ord = 4;            % Ordem do filtro
% 
% Fc1 = 40;         % F. corte analagica (FPB), Hz
% Fc2 = 0.5;        % F. corte analagica (FPA), Hz
% W1c = Fc1/Fs;
% W2c = Fc2/Fs;
% 
% %----------------------------------------------------
% % Coeficientes dos Filtros Butterworth
% [B1,A1] = butter(Ord,W1c*2,'low'); % FPB
% [B2,A2] = butter(Ord,W2c*2,'high'); % FPB
% %----------------------------------------------------
% %----------------------------------------------------
% %ecgPa = filtfilt(B2,A2,ecgRaw);    %Pasa-Baja
% ecgPb = filtfilt(B1,A1,ecgRaw);    %Pasa-Baja
% figure(1)
% plot(Vt,ecgPb)
% hold on
% grid on
