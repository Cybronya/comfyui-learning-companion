---
name: unknown_workflow_sampler_unet_vae_201
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.771667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-H3_插帧图生视频_2084843609874067458.json, 视频生成/文生视频/MiniMax-H3首尾帧生视频 5秒视频只需要3分钟+全节点注释_2084503505364148226.json, 视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_201

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3_插帧图生视频_2084843609874067458.json、视频生成/文生视频/MiniMax-H3首尾帧生视频 5秒视频只需要3分钟+全节点注释_2084503505364148226.json、视频生成/文生视频/MiniMax-lightx2v-Turbo-1.0 + Realism-People-Lora_2087508053485776898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `GetImageSize+` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `Text Find and Replace` —— 1/3 个有
- `TextOverlay` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
