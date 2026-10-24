---
name: unknown_workflow_video_lora_sampler_441
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9332
common_nodes: [LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【遇见AI】wan2.1 VACE 首尾帧_2065243346691510273.json, 视频生成/图生视频/【遇见AI】wan2.1文生视频不同加速lora对比_2062115572657254402.json, 视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json, 视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 文生视频_2070787856590786562.json, 视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_441

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/【遇见AI】wan2.1 VACE 首尾帧_2065243346691510273.json、视频生成/图生视频/【遇见AI】wan2.1文生视频不同加速lora对比_2062115572657254402.json、视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 图生视频_2070775832578191361.json、视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 文生视频_2070787856590786562.json、视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEmptyEmbeds` —— 3/5 个有
- `GetImageSize+` —— 2/5 个有
- `MaskPreview+` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `WanVideoVACEEncode` —— 2/5 个有
- `WanVideoVACEModelSelect` —— 2/5 个有
- `WanVideoVACEStartToEndFrame` —— 2/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `WanVideoVRAMManagement` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
