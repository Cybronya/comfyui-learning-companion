---
name: unknown_workflow_sampler_unet_vae_18
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.96225
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Edit_2511_2011624956571951105.json, 图片生成/图生图/Qwen_Edit_2511_3D白膜精准镜头控制之二_2009543617806864386.json, 图片生成/图生图/Qwen_Edit_2511_96个镜头精准控制_2009048922370613249.json, 图片生成/图生图/Qwen_Edit_2511_SAM3D Object精准镜头控制之三_2010203437203460098.json, 图片生成/图生图/Qwen_Edit_2511精准动作设计之一_2003647587385286658.json, 图片生成/图生图/Qwen_Edit_2511精准动作设计之二_2006926971191693314.json, 图片生成/图生图/Qwen_Edit_2511色块打光LoRA工作流_2007812725702926338.json, 图片生成/图生图/Qwen手机上的3D城市_1993197130982637570.json, 图片生成/图生图/ktv公主_1991635135160336386.json, 图片生成/图生图/qwen图生图  洗图  重绘 局部修改_2046419289288216577.json, 图片生成/图生图/产品展示 产品替换 图生图 多图编辑_2044376198586834945.json, 图片生成/图生图/产品展示 多图编辑 多图融合  图生图_2044421173475287041.json, 图片生成/图生图/产品展示 多图融合 多图编辑_2044376805544566785.json, 图片生成/图生图/产品替换 产品展示 电商 双图融合 多图编辑 多图融合  图生图_2045403356130189314.json, 图片生成/图生图/产品替换 产品展示_2045428594398208002.json, 图片生成/图生图/产品替换 双图融合 多图编辑 多图融合  图生图_2045390109431832578.json, 图片生成/图生图/人物角色-全视角参考视图_2040802253094785026.json, 图片生成/图生图/全视图 _ 角色一致性_1991419477451624450.json, 图片生成/图生图/全视图 _ 角色一致性_2007004747022213121.json, 图片生成/文生图/Qwen-image-Edit（OOTD）_1959220361894244353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_18

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Qwen_Edit_2511_2011624956571951105.json、图片生成/图生图/Qwen_Edit_2511_3D白膜精准镜头控制之二_2009543617806864386.json、图片生成/图生图/Qwen_Edit_2511_96个镜头精准控制_2009048922370613249.json、图片生成/图生图/Qwen_Edit_2511_SAM3D Object精准镜头控制之三_2010203437203460098.json、图片生成/图生图/Qwen_Edit_2511精准动作设计之一_2003647587385286658.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 19/20 个有
- `TextEncodeQwenImageEditPlus` —— 19/20 个有
- `LoraLoaderModelOnly` —— 13/20 个有
- `ConditioningZeroOut` —— 12/20 个有
- `PreviewImage` —— 8/20 个有
- `Power Lora Loader (rgthree)` —— 5/20 个有
- `Anything Everywhere3` —— 4/20 个有
- `Anything Everywhere` —— 3/20 个有
- `ConstrainImage|pysssss` —— 3/20 个有
- `JjkText` —— 2/20 个有
- `LoraLoader` —— 2/20 个有
- `ImageConcanate` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/20 个有
- `MuyeTextEditOutput` —— 1/20 个有
- `RMBG` —— 1/20 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 20 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 1024 | 928 - 1920 | 20 | 76% |
| 高度 | 1264 | 720 - 1664 | 20 | 81% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 56/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 928 - 1920，20 个样本
- 高度 中位数 1264，观测区间 720 - 1664，20 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（56/20 个样本）：Steps较低可能导致细节不足
