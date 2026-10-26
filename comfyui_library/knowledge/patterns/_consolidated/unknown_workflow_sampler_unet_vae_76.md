---
name: unknown_workflow_sampler_unet_vae_76
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.985909
common_nodes: [CFGNorm, CLIPLoader, KSampler, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Edit_2511_2011624956571951105.json, 图片生成/图生图/Qwen_Edit_2511_3D白膜精准镜头控制之二_2009543617806864386.json, 图片生成/图生图/Qwen_Edit_2511_96个镜头精准控制_2009048922370613249.json, 图片生成/图生图/Qwen_Edit_2511_SAM3D Object精准镜头控制之三_2010203437203460098.json, 图片生成/图生图/Qwen_Edit_2511精准动作设计之一_2003647587385286658.json, 图片生成/图生图/Qwen_Edit_2511精准动作设计之二_2006926971191693314.json, 图片生成/图生图/Qwen_Edit_2511色块打光LoRA工作流_2007812725702926338.json, 图片生成/图生图/Qwen手机上的3D城市_1993197130982637570.json, 图片生成/图生图/anime2real-2511动漫转真人工作流alpha_2008554085934440450.json, 图片生成/图生图/anime2real-2511动漫转真人工作流正式版_2008849773113118722.json, 图片生成/图生图/anime2real-2511动漫转真人工作流正式版_2019037044483301378.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_76

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen_Edit_2511_2011624956571951105.json、图片生成/图生图/Qwen_Edit_2511_3D白膜精准镜头控制之二_2009543617806864386.json、图片生成/图生图/Qwen_Edit_2511_96个镜头精准控制_2009048922370613249.json、图片生成/图生图/Qwen_Edit_2511_SAM3D Object精准镜头控制之三_2010203437203460098.json、图片生成/图生图/Qwen_Edit_2511精准动作设计之一_2003647587385286658.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `EmptyLatentImage` —— 8/11 个有
- `Power Lora Loader (rgthree)` —— 5/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `AddLabel` —— 3/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 3/11 个有
- `Label (rgthree)` —— 2/11 个有
- `LoraLoader` —— 2/11 个有
- `Textbox` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 11 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1520 | 1024 - 1920 | 8 | 80% |
| 高度 | 1080 | 720 - 1280 | 8 | 86% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，11 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1520，观测区间 1024 - 1920，8 个样本，取值集中（一致性 80%）
- 高度 中位数 1080，观测区间 720 - 1280，8 个样本，取值集中（一致性 86%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
