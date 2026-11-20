---
name: unknown_workflow_lora_sampler_clip_65
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.943143
common_nodes: [ApplyFBCacheOnModel, BNK_CLIPTextEncodeAdvanced, CheckpointLoaderSimple, EmptyLatentImage, HyperLoRAApplyLoRA, HyperLoRAConfig, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, HyperLoRAIDCond, HyperLoRALoader, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/HyperLora+InstantID 人物一致性_1919998125195329537.json, 图片生成/图生图/hyperlora人物一致性生成模型（字节）_1916665695336071169.json, 图片生成/图生图/多图参考+精准换脸 ｜Hyper LoRA 和 InstantID_1921206761012002817.json, 图片生成/文生图/HyperLoRA+InstantID 人物一致性_1918136035447083009.json, 图片生成/文生图/HyperLoRA人物一致性生图_1918130332774629377.json, 图片生成/文生图/HyperLora-InstantID人脸一致性-超级加速文生图-自用_1973749895905587201.json, 图片生成/文生图/HyperLora人物一致性CN控制文生图（人物及姿势参考版）_1915753672788082690.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/HyperLora+InstantID 人物一致性_1919998125195329537.json、图片生成/图生图/hyperlora人物一致性生成模型（字节）_1916665695336071169.json、图片生成/图生图/多图参考+精准换脸 ｜Hyper LoRA 和 InstantID_1921206761012002817.json、图片生成/文生图/HyperLoRA+InstantID 人物一致性_1918136035447083009.json、图片生成/文生图/HyperLoRA人物一致性生图_1918130332774629377.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `BNK_CLIPTextEncodeAdvanced`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `HyperLoRAApplyLoRA`
- `HyperLoRAConfig`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `HyperLoRAIDCond`
- `HyperLoRALoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ControlNetLoader` —— 6/7 个有
- `ImpactMakeImageBatch` —— 6/7 个有
- `ApplyInstantIDAdvanced` —— 5/7 个有
- `CLIPSetLastLayer` —— 5/7 个有
- `InstantIDFaceAnalysis` —— 5/7 个有
- `InstantIDModelLoader` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `ImageConcanate` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ControlNetApplyAdvanced` —— 1/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `FloatConstant` —— 1/7 个有
- `Int` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有
- `Text Concatenate (JPS)` —— 1/7 个有
- `Video_Upscale_With_Model` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 7 | 91% |
| 高度 | 1024 | 1024 - 1280 | 7 | 92% |
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 3 | 3 - 5 | 7 | 74% |
| 采样算法 | dpmpp_2m | - | 7 | 100% |
| 调度器 | karras | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，7 个样本，取值集中（一致性 91%）
- 高度 中位数 1024，观测区间 1024 - 1280，7 个样本，取值集中（一致性 92%）
- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 5，7 个样本
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 100%
- 调度器 最常用 karras，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
