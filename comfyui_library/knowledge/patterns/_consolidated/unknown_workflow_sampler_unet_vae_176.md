---
name: unknown_workflow_sampler_unet_vae_176
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.835333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/海螺H3首尾帧生视频_2087721274360553473.json, 视频生成/文生视频/首尾帧加速图minimax_h3_lightx2v生文生ENG_2087087697318998017.json, 视频生成/文生视频/首尾帧生视频+_2084526811551195138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_176

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/海螺H3首尾帧生视频_2087721274360553473.json、视频生成/文生视频/首尾帧加速图minimax_h3_lightx2v生文生ENG_2087087697318998017.json、视频生成/文生视频/首尾帧生视频+_2084526811551195138.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `BOOLConstant` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `easy imageIndexSwitch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
