---
name: unknown_workflow_sampler_unet_vae_191
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.808571
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, PreviewAny, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json, 图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json, 图片生成/图生图/姿势迁移-qwen21_2105531509292752897.json, 图片生成/图生图/绅士私房写真图片qwen21_2105590393751560193.json, 图片生成/图生图/角色头部替换qwen21_2105521210460303362.json, 图片生成/文生图/厚涂cg-qwen21_2106296350756401153.json, 平台全量/图片转白膜-qwen21_2117404595398991874.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_191

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json、图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json、图片生成/图生图/姿势迁移-qwen21_2105531509292752897.json、图片生成/图生图/绅士私房写真图片qwen21_2105590393751560193.json、图片生成/图生图/角色头部替换qwen21_2105521210460303362.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 6/7 个有
- `easy clearCacheAll` —— 6/7 个有
- `easy imageConcat` —— 5/7 个有
- `ImageScaleBy` —— 4/7 个有
- `Label (rgthree)` —— 3/7 个有
- `LoraLoaderBypassModelOnly` —— 2/7 个有
- `PIP_图像联结` —— 2/7 个有
- `CR Prompt List` —— 1/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 30 | 30 - 40 | 7 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 40，7 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
