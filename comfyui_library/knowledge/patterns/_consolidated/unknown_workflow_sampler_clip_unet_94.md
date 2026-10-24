---
name: unknown_workflow_sampler_clip_unet_94
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8697
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EasyCache, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json, comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json, 视频生成/图生视频/(2倍加速)HunyuanVideo 1.5 720P 20步优化版图生视频_1992829653211738114.json, 视频生成/图生视频/HunyuanVideo 1.5 720P 20步优化版图生视频_1992813582438166529.json, 视频生成/图生视频/HunyuanVideo 1.5 720P 图生视频优化版_1992895352435003394.json, 视频生成/图生视频/HunyuanVideo 1.5 版图生视频_1992883581467029505.json, 视频生成/图生视频/video_hunyuan_video_1.5_720p_i2v-混元Video1.5大模型——图生视频工作流_1994018725741477890.json, 视频生成/图生视频/图生视频 _ 支持文字 HunyuanVideo1.5_1996147108740808705.json, 视频生成/图生视频/混元Video1.5大模型——图生视频工作流_1993514480827121665.json, 视频生成/文生视频/Hunyuan_Video_1.5_720p_i2v + Upscaler_1998064669535404034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json、comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json、视频生成/图生视频/(2倍加速)HunyuanVideo 1.5 720P 20步优化版图生视频_1992829653211738114.json、视频生成/图生视频/HunyuanVideo 1.5 720P 20步优化版图生视频_1992813582438166529.json、视频生成/图生视频/HunyuanVideo 1.5 720P 图生视频优化版_1992895352435003394.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EasyCache`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 9/10 个有
- `CLIPVisionLoader` —— 9/10 个有
- `HunyuanVideo15ImageToVideo` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `JWInteger` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `DisableNoise` —— 4/10 个有
- `HunyuanVideo15LatentUpscaleWithModel` —— 4/10 个有
- `HunyuanVideo15SuperResolution` —— 4/10 个有
- `LatentUpscaleModelLoader` —— 4/10 个有
- `SplitSigmas` —— 4/10 个有
- `Label (rgthree)` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `DF_Int_to_Float` —— 1/10 个有
- `EmptyHunyuanVideo15Latent` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `RH_Translator` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
