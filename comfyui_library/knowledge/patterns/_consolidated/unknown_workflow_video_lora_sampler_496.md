---
name: unknown_workflow_video_lora_sampler_496
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.49275
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Divide [DVB], FlashVSRNode, Float, GetNode, ImageResizeKJv2, Int, JWInteger, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SigmasGraph, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 图生_首尾帧生视频_2094253699223875585.json, 视频生成/图生视频/MiniMax H3 多图参考生视频_2089995096556130306.json, 视频生成/图生视频/MiniMax H3 音频驱动数字人_2089949306781519874.json, 视频生成/文生视频/MiniMax H3 文生视频+FlashVSR高清_2089958386669543425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_496

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生_首尾帧生视频_2094253699223875585.json、视频生成/图生视频/MiniMax H3 多图参考生视频_2089995096556130306.json、视频生成/图生视频/MiniMax H3 音频驱动数字人_2089949306781519874.json、视频生成/文生视频/MiniMax H3 文生视频+FlashVSR高清_2089958386669543425.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Divide [DVB]`
- `FlashVSRNode`
- `Float`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SigmasGraph`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `LoadAudio` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `SDVN Fast Groups Bypasser` —— 1/4 个有
- `SoundFlow_GetLength` —— 1/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/4 个有
- `ZNGB_AudioCrop` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
