---
name: text_to_image_sampler_clip_unet_16
type: Text To Image
frequency: 19
level: moderate
coverage: 0.68
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Turbo文生图V1_2069662522738831362.json, 图片生成/文生图/Krea2 Turbo文生图V1_2070018860480286722.json, 图片生成/文生图/Krea2 Turbo文生图（双采版）_2070485457284190209.json, 图片生成/文生图/Krea2 文生图极速版_2075489210370445314.json, 图片生成/文生图/Krea2-Turbo-文生图_2069949151932149761.json, 图片生成/文生图/Krea2_turbo_文生图_2066148990659416066.json, 图片生成/文生图/Krea2_turbo基础工作流（官方版本构架微调）_2083013364665643010.json, 图片生成/文生图/Krea2文生图+提示词反推Turbo+Realism+Engineer+V2_2072569695793926145.json, 图片生成/文生图/image_krea2_turbo_t2i_2069968212200087553.json, 图片生成/文生图/image_krea2_turbo_t2i_2072904099296800770.json, 图片生成/文生图/image_krea2_turbo_t2i_2079183226878382082.json, 图片生成/文生图/image_krea2_turbo_t2i_2099207878002429953.json, 图片生成/文生图/image_krea2_turbo文生图_2074494308316700673.json, 图片生成/文生图/krea2-turbo-文生图-(fp8)_2110683456106754049.json, 图片生成/文生图/krea2_turbo_t2i_api_2098965323885146113.json, 图片生成/文生图/图图小脸蛋 KREA2 工作流_2072299896564178946.json, 图片生成/文生图/图图的标准KREA2 TURBO 工作流（附带官方提示词优化功能）_2070019455769473025.json, 图片生成/文生图/文生图_krea2_2072153299662495745.json, 图片生成/文生图/最新文生图Krea2+Turbo 双采样加强版_2071101261251960834.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_16

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/Krea2 Turbo文生图V1_2069662522738831362.json、图片生成/文生图/Krea2 Turbo文生图V1_2070018860480286722.json、图片生成/文生图/Krea2 Turbo文生图（双采版）_2070485457284190209.json、图片生成/文生图/Krea2 文生图极速版_2075489210370445314.json、图片生成/文生图/Krea2-Turbo-文生图_2069949151932149761.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 18/19 个有
- `StringConcatenate` —— 17/19 个有
- `TextGenerate` —— 17/19 个有
- `ResolutionSelector` —— 14/19 个有
- `LoraLoaderModelOnly` —— 13/19 个有
- `ComfySwitchNode` —— 12/19 个有
- `PrimitiveBoolean` —— 12/19 个有
- `Int` —— 3/19 个有
- `LoadImage` —— 3/19 个有
- `Fast Groups Bypasser (rgthree)` —— 2/19 个有
- `PreviewImage` —— 2/19 个有
- `RH_Captioner` —— 2/19 个有
- `Power Lora Loader (rgthree)` —— 1/19 个有
- `PrimitiveInt` —— 1/19 个有
- `easy positive` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 19 | 72% |
| 高度 | 1024 | 1024 - 2048 | 19 | 72% |
| 采样步数 | 8 | 6 - 9 | 19 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 89% |
| 重绘幅度 | 1 | 0.4 - 1 | 19 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，19 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，19 个样本
- 采样步数 中位数 8，观测区间 6 - 9，19 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，19 个样本，取值集中（一致性 80%）
- 高发问题（21/19 个样本）：Steps较低可能导致细节不足
