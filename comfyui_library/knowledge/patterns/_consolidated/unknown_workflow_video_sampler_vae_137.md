---
name: unknown_workflow_video_sampler_vae_137
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88125
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, HyVideoBlockSwap, HyVideoDecode, HyVideoEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTextEmbedBridge, HyVideoVAELoader, ImageConcatMulti, ImageResizeKJv2, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, PreviewImage, TTP_Expand_And_Mask, TextEncodeHunyuanVideo_ImageToVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/单主体HuyuanCustom视频编辑一致性工作流优化版V1_1920816931887321089.json, 视频生成/图生视频/双主体加速HuyuanCustom强一致性高稳定性视频编辑V3_1921095971592159233.json, 视频生成/图生视频/双图加速HuyuanCustom强一致性视频_1923619819957252098.json, 视频生成/图生视频/多主体HuyuanCustom视频编辑一致性工作流优化版V2(修复)_1920773732279980033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_137

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/单主体HuyuanCustom视频编辑一致性工作流优化版V1_1920816931887321089.json、视频生成/图生视频/双主体加速HuyuanCustom强一致性高稳定性视频编辑V3_1921095971592159233.json、视频生成/图生视频/双图加速HuyuanCustom强一致性视频_1923619819957252098.json、视频生成/图生视频/多主体HuyuanCustom视频编辑一致性工作流优化版V2(修复)_1920773732279980033.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTextEmbedBridge`
- `HyVideoVAELoader`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `PreviewImage`
- `TTP_Expand_And_Mask`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `HyVideoLoraSelect` —— 3/4 个有
- `HyVideoTeaCache` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `JWImageResizeByLongerSide` —— 3/4 个有
- `HunyuanVideoFresca` —— 2/4 个有
- `HunyuanVideoSLG` —— 2/4 个有
- `HyVideoTorchCompileSettings` —— 2/4 个有
- `Bjornulf_ShowJson` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
