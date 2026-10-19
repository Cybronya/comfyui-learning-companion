---
name: unknown_workflow_sampler_unet_vae_77
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.832889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax h3多元素参考 生视频工作流_2084531165620432897.json, 视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json, 视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json, 视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json, 视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json, 视频生成/文生视频/Minimax H3 加速工作流_2085691765964754946.json, 视频生成/文生视频/Minimax H3多参视频生成+全节点注释_2084873538615472129.json, 视频生成/文生视频/MinimaxH3多参生视频+(量化加速版)_2084546214854483969.json, 视频生成/文生视频/minimax 首尾帧加速版_2084471697830404098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_77

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/minimax h3多元素参考 生视频工作流_2084531165620432897.json、视频生成/图生视频/minimax 首尾帧加速版_2089263810258497538.json、视频生成/图生视频/minimax_H3_r2v 2倍加速_2084977611708657665.json、视频生成/图生视频/minimax_H3_r2v 4步lora加速_2085423519835447298.json、视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PathchSageAttentionKJ` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `LoadAudio` —— 7/9 个有
- `MiniMaxH3ReferenceToVideo` —— 7/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `ComfyMathExpression` —— 6/9 个有
- `PrimitiveFloat` —— 6/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/9 个有
- `EasyCache` —— 4/9 个有
- `ResizeImagesByLongerEdge` —— 4/9 个有
- `Int` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `ImageResize+` —— 2/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `MiniMaxH3ImageToVideo` —— 2/9 个有
- `RTXVideoSuperResolution` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `LoraLoaderBypassModelOnly` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
