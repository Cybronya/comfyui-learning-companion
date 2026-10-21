---
name: unknown_workflow_video_lora_sampler_211
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.87
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, Fast Groups Bypasser (rgthree), GuHaiAutoImageSplit, ImageScaleToTotalPixels, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PreviewImage, SamplerCustom, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2078887009887809537.json, 视频生成/图生视频/2063484969040834562.json, 视频生成/图生视频/2063953334742114305.json, 视频生成/图生视频/2063277846595981313.json, 视频生成/图生视频/2063095957193056258.json, 视频生成/图生视频/2064190064883757058.json, 视频生成/图生视频/2070140251913412610.json, 视频生成/图生视频/2063451462600052737.json, 视频生成/图生视频/2077620703326728194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_211

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2078887009887809537.json、视频生成/图生视频/2063484969040834562.json、视频生成/图生视频/2063953334742114305.json、视频生成/图生视频/2063277846595981313.json、视频生成/图生视频/2063095957193056258.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GuHaiAutoImageSplit`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LTXDirectorGuide` —— 7/9 个有
- `YusuLTXDirector` —— 6/9 个有
- `CheckpointLoaderSimple` —— 5/9 个有
- `CreateVideo` —— 5/9 个有
- `GetVideoComponents` —— 5/9 个有
- `UNETLoader` —— 4/9 个有
- `孤海注释` —— 3/9 个有
- `Label (rgthree)` —— 2/9 个有
- `Yusu-LTXDirector` —— 2/9 个有
- `YusuLTXDirectorGuide` —— 2/9 个有
- `CS-LTXGridDirector` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PreviewAny` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
