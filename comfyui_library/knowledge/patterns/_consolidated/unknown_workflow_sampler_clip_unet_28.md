---
name: unknown_workflow_sampler_clip_unet_28
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.876
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json, comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json, 视频生成/图生视频/1992829653211738114.json, 视频生成/图生视频/1992813582438166529.json, 视频生成/图生视频/1992895352435003394.json, 视频生成/图生视频/1992883581467029505.json, 视频生成/图生视频/1996147108740808705.json, 视频生成/图生视频/1993514480827121665.json, 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p_1993246112486195202.json, 视频生成/文生视频/HunyuanVideo_1.5加速图生视频1080p（熊叔版）_1993572660164706305.json, 视频生成/文生视频/HunyuanVideo_1.5加速文生视频1080p_1993277000070660097.json, 视频生成/文生视频/Hunyuan_Video_1.5_720p_i2v + Upscaler_1998064669535404034.json, 视频生成/文生视频/混元Video1.5大模型——文生视频工作流_1993513786705379330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_i2v.json、comfyui-workflow-templates-json/video_hunyuan_video_1.5_720p_t2v.json、视频生成/图生视频/1992829653211738114.json、视频生成/图生视频/1992813582438166529.json、视频生成/图生视频/1992895352435003394.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
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
- `CLIPVisionEncode` —— 10/13 个有
- `CLIPVisionLoader` —— 10/13 个有
- `EasyCache` —— 10/13 个有
- `HunyuanVideo15ImageToVideo` —— 10/13 个有
- `LoadImage` —— 10/13 个有
- `DisableNoise` —— 8/13 个有
- `HunyuanVideo15LatentUpscaleWithModel` —— 8/13 个有
- `HunyuanVideo15SuperResolution` —— 8/13 个有
- `LatentUpscaleModelLoader` —— 8/13 个有
- `SplitSigmas` —— 8/13 个有
- `JWInteger` —— 5/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/13 个有
- `EmptyHunyuanVideo15Latent` —— 3/13 个有
- `Label (rgthree)` —— 3/13 个有
- `LoraLoaderModelOnly` —— 3/13 个有
- `PathchSageAttentionKJ` —— 3/13 个有
- `CR Text` —— 1/13 个有
- `DF_Int_to_Float` —— 1/13 个有
- `JjkText` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
