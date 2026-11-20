---
name: text_to_image_sampler_clip_unet_47
type: Text To Image
frequency: 12
level: moderate
coverage: 0.970583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima_base_原版基础工作流_2055104883111546881.json, 图片生成/文生图/Anima_base_原版基础工作流_2055127367860932609.json, 图片生成/文生图/Anima动漫生成大模型：一键生成“良子”漫画插图！_2018308287694905346.json, 图片生成/文生图/Anima基础工作流_2018148600248803330.json, 图片生成/文生图/Anima文生图_2021929707570208769.json, 图片生成/文生图/Anima最新动漫文生图模型_2018217761347997698.json, 图片生成/文生图/Beyond Reality Z-image文生图_1999838076270768130.json, 图片生成/文生图/Boogu 文生图_2068696295937765378.json, 图片生成/文生图/Boogu-Image Base+Turbe双采文生图2606_2068416769479499777.json, 图片生成/文生图/Krea2 快速生图_2082367532186554370.json, 图片生成/文生图/Lens-文生图_2058748909492723713.json, 图片生成/文生图/PromptLine+Anima Preview2艺术家批量风格测试_2033542990416846849.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Anima_base_原版基础工作流_2055104883111546881.json、图片生成/文生图/Anima_base_原版基础工作流_2055127367860932609.json、图片生成/文生图/Anima动漫生成大模型：一键生成“良子”漫画插图！_2018308287694905346.json、图片生成/文生图/Anima基础工作流_2018148600248803330.json、图片生成/文生图/Anima文生图_2021929707570208769.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/12 个有
- `LatentUpscaleBy` —— 3/12 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/12 个有
- `GPTImage2PromptPreview` —— 1/12 个有
- `JWStringConcat` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `String Literal` —— 1/12 个有
- `easy promptLine` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 40 | 12 | 51% |
| Prompt 约束强度(CFG) | 3.75 | 1 - 5 | 12 | 48% |
| 采样算法 | er_sde | - | 12 | 50% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 0.35 - 1 | 12 | 79% |
| 宽度 | 932 | 720 - 1280 | 12 | 86% |
| 高度 | 1152 | 1024 - 1600 | 12 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 40，12 个样本
- Prompt 约束强度(CFG) 中位数 3.75，观测区间 1 - 5，12 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 er_sde，12 个样本，一致性 50%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，12 个样本
- 宽度 中位数 932，观测区间 720 - 1280，12 个样本，取值集中（一致性 86%）
- 高度 中位数 1152，观测区间 1024 - 1600，12 个样本，取值集中（一致性 84%）
