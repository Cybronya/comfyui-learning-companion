---
name: unknown_workflow_sampler_clip_unet_214
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9685
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/低精图洗图+服装替换_2085353987464847361.json, 图片生成/图生图/图案转刺绣风格_2043579107664994306.json, 图片生成/图生图/多图编辑组合_2078268396902379521.json, 图片生成/图生图/换装Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2012781629911076866.json, 图片生成/图生图/换装换脸_优化升级_姿态动作迁移_多图编辑加速版_2064901253225869314.json, 图片生成/图生图/精准换脸换头 换脸换装多图编辑+人物一致+自然真实+多图编辑加速版_2088433029512519682.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_214

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/低精图洗图+服装替换_2085353987464847361.json、图片生成/图生图/图案转刺绣风格_2043579107664994306.json、图片生成/图生图/多图编辑组合_2078268396902379521.json、图片生成/图生图/换装Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2012781629911076866.json、图片生成/图生图/换装换脸_优化升级_姿态动作迁移_多图编辑加速版_2064901253225869314.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `EmptyFlux2LatentImage` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `JWFloat` —— 3/6 个有
- `AspectRatioSelect` —— 2/6 个有
- `RH_RhartImageG2ImageToImage` —— 2/6 个有
- `easy imageColorMatch` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `AspectRatio` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `Display Any (rgthree)` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `Qwen3VL_Chat` —— 1/6 个有
- `Seed_` —— 1/6 个有
- `ttN text` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
