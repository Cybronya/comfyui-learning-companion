---
name: unknown_workflow_sampler_unet_vae_231
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.942833
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/qwen_edit_2509童装上身工作流_2010558260528553985.json, 图片生成/图生图/【遇见AI】Qwen-image 文生图基础_2050874058291593218.json, 图片生成/图生图/万物皆可Q：IP角色一键智绘Q版风格_2056237735295410178.json, 图片生成/图生图/人物图像拼合_2042497116639076354.json, 图片生成/图生图/人物图像生成动漫Q版动画人物IP角色一键智绘Q版风格_2077294254203949058.json, 图片生成/图生图/千问图像编辑2511 双图编辑一致性_2013173412998418434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_231

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/qwen_edit_2509童装上身工作流_2010558260528553985.json、图片生成/图生图/【遇见AI】Qwen-image 文生图基础_2050874058291593218.json、图片生成/图生图/万物皆可Q：IP角色一键智绘Q版风格_2056237735295410178.json、图片生成/图生图/人物图像拼合_2042497116639076354.json、图片生成/图生图/人物图像生成动漫Q版动画人物IP角色一键智绘Q版风格_2077294254203949058.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `VAEDecode` —— 5/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/6 个有
- `Easy_QwenEdit2509` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `TextEncodeQwenImageEditPlus` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `Int` —— 1/6 个有
- `TT_img_enc` —— 1/6 个有
- `TextInputNode` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `VAEDecodeTiled` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 40 | 6 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 53% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 40，6 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
