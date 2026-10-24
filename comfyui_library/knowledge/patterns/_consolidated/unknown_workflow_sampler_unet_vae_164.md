---
name: unknown_workflow_sampler_unet_vae_164
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.815167
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, PreviewAny, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json, 图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json, 图片生成/图生图/姿势迁移-qwen21_2105531509292752897.json, 图片生成/图生图/绅士私房写真图片qwen21_2105590393751560193.json, 图片生成/图生图/角色头部替换qwen21_2105521210460303362.json, 图片生成/文生图/厚涂cg-qwen21_2106296350756401153.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_164

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-2.1角色卡立绘_2102980604450140162.json、图片生成/图生图/一键制作人物风格信息图--Qwen image 2.1_2105302134995644418.json、图片生成/图生图/姿势迁移-qwen21_2105531509292752897.json、图片生成/图生图/绅士私房写真图片qwen21_2105590393751560193.json、图片生成/图生图/角色头部替换qwen21_2105521210460303362.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
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
- `JjkText` —— 5/6 个有
- `easy clearCacheAll` —— 5/6 个有
- `easy imageConcat` —— 4/6 个有
- `ImageScaleBy` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `PIP_图像联结` —— 2/6 个有
- `CR Prompt List` —— 1/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `LoraLoaderBypassModelOnly` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 35 | 30 - 40 | 6 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 35，观测区间 30 - 40，6 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
