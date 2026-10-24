---
name: unknown_workflow_sampler_unet_vae_197
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8104
common_nodes: [CLIPLoader, KSampler, LoadImage, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json, 图片生成/图生图/Qwen21_1底图5参考_带宽高_2112762005873582081.json, 图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json, 图片生成/图生图/qwen_image_2.1图像编辑_2103699751001747458.json, 图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_197

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json、图片生成/图生图/Qwen21_1底图5参考_带宽高_2112762005873582081.json、图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json、图片生成/图生图/qwen_image_2.1图像编辑_2103699751001747458.json、图片生成/文生图/Qwen-image2.1多视图_角色三视图_2103002508884008961.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `Anything Everywhere3` —— 2/5 个有
- `EmptyImage` —— 2/5 个有
- `ImageCompositeMasked` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `llama_cpp_instruct_adv` —— 1/5 个有
- `llama_cpp_model_loader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
