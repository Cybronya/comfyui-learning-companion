---
name: unknown_workflow_inpaint_sampler_clip_40
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.859333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/生图-图像局部重绘-OneReward-Fill_1979572091114655745.json, 图片生成/图生图/生图-图像擦除-OneReward-Fill_1979563638967144449.json, 平台全量/006.擦除OneReward_2003072426583949314.json, 平台全量/万物消除_快速版_2039908640630509570.json, 平台全量/无损移除logo、水印、文字_2010689062901915649.json, 平台全量/🆓OneReward-Fill最强移除+重绘_1983904162037563393.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/生图-图像局部重绘-OneReward-Fill_1979572091114655745.json、图片生成/图生图/生图-图像擦除-OneReward-Fill_1979563638967144449.json、平台全量/006.擦除OneReward_2003072426583949314.json、平台全量/万物消除_快速版_2039908640630509570.json、平台全量/无损移除logo、水印、文字_2010689062901915649.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 5/6 个有
- `LayerMask: MaskGrow` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `ColorCorrect` —— 4/6 个有
- `ImpactInt` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `ToBinaryMask` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `CR Latent Batch Size` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `ImageConcanate` —— 2/6 个有
- `LayerUtility: ImageScaleRestore V2` —— 2/6 个有
- `easy seed` —— 2/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `Fast Bypasser (rgthree)` —— 1/6 个有
- `GoogleTranslateTextNode` —— 1/6 个有
- `Mask Fill Holes` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 12 - 30 | 6 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 12 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
