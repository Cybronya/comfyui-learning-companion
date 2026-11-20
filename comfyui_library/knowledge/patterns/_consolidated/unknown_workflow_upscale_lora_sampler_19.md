---
name: unknown_workflow_upscale_lora_sampler_19
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.931
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Edit_2509 人物多角度镜头+放大_1985880356014497794.json, 图片生成/图生图/分镜   图生图  多视图  多角度  多视角  Qwen_Edit_2511_2082898294979780610.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2079632388715536385.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2080156840373088258.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2080938350600609794.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2081734985232506881.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2081737146230202370.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2081916835062181889.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2082177387202174978.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2083971939718221826.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2084155308896776193.json, 图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2085226446498390017.json, 平台全量/提示词- 多视角 多角度 三视图千问2511+放大_2063980923514871810.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen_Edit_2509 人物多角度镜头+放大_1985880356014497794.json、图片生成/图生图/分镜   图生图  多视图  多角度  多视角  Qwen_Edit_2511_2082898294979780610.json、图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2079632388715536385.json、图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2080156840373088258.json、图片生成/图生图/分镜图生图  多视图  多角度  多视角  Qwen_Edit_2511_2080938350600609794.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `ImpactInt` —— 1/13 个有
- `NunchakuQwenImageDiTLoader` —— 1/13 个有
- `NunchakuQwenImageLoraStackV2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
