#include "InttConversion.h"

void temp_bkg(TCanvas * c1,string mode, int color_step, double peek)
{
    c1 -> cd();

    int N_ladder[4] = {12, 12, 16, 16};
    string ladder_index_string[16] = {"00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15"};

    vector<double> x_vec; x_vec.clear();
    vector<double> y_vec; y_vec.clear();

    vector<double> x_vec_2; x_vec_2.clear();
    vector<double> y_vec_2; y_vec_2.clear();

    for (int server_i = 0; server_i < 4; server_i++)
    {
        for (int FC_i = 0; FC_i < 14; FC_i++)
        {
            for (int chan_i = 0; chan_i < 128; chan_i++)
            {

                x_vec.push_back(InttConversion::Get_XY_all(Form("intt%i",server_i),FC_i,14,chan_i,mode,peek).x);
                y_vec.push_back(InttConversion::Get_XY_all(Form("intt%i",server_i),FC_i,14,chan_i,mode,peek).y);

                x_vec_2.push_back(InttConversion::Get_XY_all(Form("intt%i",server_i),FC_i,1,chan_i,mode,peek).x);
                y_vec_2.push_back(InttConversion::Get_XY_all(Form("intt%i",server_i),FC_i,1,chan_i,mode,peek).y);
                // cout<<"("<<InttConversion::Get_XY_all(Form("intt%i",server_i),FC_i,14,chan_i).first<<","<<InttConversion::Get_XY_all(Form("intt%i",server_i),FC_i,14,chan_i).second<<"),";

                // cout<<"("<<Get_XY_all(Form("%s%s",layer_text[i].c_str(),ladder_index_string[i1].c_str()),used_chip,127).first<<","<<Get_XY_all(Form("%s%s",layer_text[i].c_str(),ladder_index_string[i1].c_str()),used_chip,127).second<<")";
            }
        }
    }

    TGraph * aaa = new TGraph(x_vec.size(),&x_vec[0],&y_vec[0]);
    aaa -> SetMarkerStyle(20);
    aaa -> SetMarkerSize(0.1);
    aaa -> SetMarkerColor(4 + color_step);

    aaa -> GetXaxis() -> SetTitle("X axis (mm)");
    aaa -> GetYaxis() -> SetTitle("Y axis (mm)");

    TGraph * bbb = new TGraph(x_vec_2.size(),&x_vec_2[0],&y_vec_2[0]);
    bbb -> SetMarkerStyle(20);
    bbb -> SetMarkerSize(0.1);
    bbb -> SetMarkerColor(4 + color_step);

    vector<double> origin_x_vec={0,0};
    vector<double> origin_y_vec={0,5};
    TGraph * origin_g = new TGraph(origin_x_vec.size(),&origin_x_vec[0],&origin_y_vec[0]);
    origin_g -> SetMarkerStyle(20);
    origin_g -> SetMarkerSize(0.5);
    origin_g -> SetMarkerColor(4 + color_step);

    
    
    aaa -> Draw("p same");
    bbb -> Draw("p same");
    origin_g -> Draw("psame");
}

void check_correction ()
{
    TCanvas * c1 = new TCanvas("","",800,800);
    c1 -> cd();

    TGraph * dddd = new TGraph();
    dddd -> SetPoint(0,0,0);
    dddd->GetXaxis()->SetLimits(-150,150);
    dddd->GetYaxis()->SetRangeUser(-150,150);

    dddd -> Draw("ap");

    temp_bkg(c1, "survey_1_XYAlpha", 0,5);

    cout<<"---------------------------------"<<endl;

    temp_bkg(c1, "survey_1_XYAlpha_Peek", 3,5);
}