---
name: unknown_workflow_sampler_clip_unet_160
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9255
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX3加速版文生图_2111042458221113346.json, 图片生成/文生图/FLUX3加速版文生图_2111059202943836161.json, 图片生成/文生图/FLUX3加速版文生图v1_2110849481448181762.json, 图片生成/文生图/FLUX3文生图sd-int8-提示词PE优化版_2111437431227641858.json, 图片生成/文生图/FLUX3文生图sd-int8-提示词pe优化版-v2_2111500134445043714.json, 图片生成/文生图/FLUX3文生图sd-int8-提示词pe优化版_2111318686400335873.json, 图片生成/文生图/Flux3+PE提示词强化加速版多图编辑_2111485757222383618.json, 视频生成/图生视频/Flux3加速版多图编辑V1_2110847111846780929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_160

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/FLUX3加速版文生图_2111042458221113346.json、图片生成/文生图/FLUX3加速版文生图_2111059202943836161.json、图片生成/文生图/FLUX3加速版文生图v1_2110849481448181762.json、图片生成/文生图/FLUX3文生图sd-int8-提示词PE优化版_2111437431227641858.json、图片生成/文生图/FLUX3文生图sd-int8-提示词pe优化版-v2_2111500134445043714.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/8 个有
- `easy showAnything` —— 3/8 个有
- `Flux3PELoader` —— 2/8 个有
- `Flux3PromptEnhance` —— 2/8 个有
- `GetLatentSize` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `QwenPERewriteT8` —— 2/8 个有
- `ReferenceMultiLatent` —— 2/8 个有
- `孤海注释` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
