---
name: unknown_workflow_sampler_unet_vae_138
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.902833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax h3多元素参考 生视频工作流_2084531165620432897.json, 视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json, 视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json, 视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json, 视频生成/文生视频/MinimaxH3多参生视频+(量化加速版)_2084546214854483969.json, 视频生成/文生视频/minimax 首尾帧加速版_2084471697830404098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_138

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/minimax h3多元素参考 生视频工作流_2084531165620432897.json、视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json、视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json、视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json、视频生成/文生视频/MinimaxH3多参生视频+(量化加速版)_2084546214854483969.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `MiniMaxH3ReferenceToVideo` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `ResizeImagesByLongerEdge` —— 4/6 个有
- `ComfyMathExpression` —— 3/6 个有
- `Int` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `EasyCache` —— 2/6 个有
- `ImageResize+` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `RTXVideoSuperResolution` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LoraLoaderBypassModelOnly` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
