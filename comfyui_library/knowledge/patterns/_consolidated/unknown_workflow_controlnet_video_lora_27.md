---
name: unknown_workflow_controlnet_video_lora_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5445
common_nodes: [CLIPVisionLoader, CR Prompt Text, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageCropByMaskAndResize, ImageFromBatch+, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM, PixelPerfectResolution, PreviewImage, SetNode, SimpleMath+, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2073284588327235586.json, 视频生成/图生视频/2073284165830795265.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2073284588327235586.json、视频生成/图生视频/2073284165830795265.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `PixelPerfectResolution`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | beta57 | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
