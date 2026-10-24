---
name: text_to_image_lora_sampler_clip_301
type: Text To Image
frequency: 6
level: strong
coverage: 0.888333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Outpaint LoRA图像扩图目前最佳｜Krea2图生图扩图工作流_2087211988345769985.json, 图片生成/图生图/Qwen Image 2.1图生图三套夏装工作流，图生图服装展示处理工具_2108281083262488578.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102105087035400194.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102483334352953345.json, 图片生成/图生图/Qwen Image 2.1自动抠图透明背景，图生图一键去底处理工具_2103602803808759810.json, 图片生成/图生图/Qwen image2.1多图编辑实用版｜多张图片统一处理｜其它图片处理通吃_2102216509333528578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_301

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Outpaint LoRA图像扩图目前最佳｜Krea2图生图扩图工作流_2087211988345769985.json、图片生成/图生图/Qwen Image 2.1图生图三套夏装工作流，图生图服装展示处理工具_2108281083262488578.json、图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102105087035400194.json、图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102483334352953345.json、图片生成/图生图/Qwen Image 2.1自动抠图透明背景，图生图一键去底处理工具_2103602803808759810.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 5/6 个有
- `TextEncodeQwenImage21` —— 5/6 个有
- `ComfySwitchNode` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `ResolutionSelector` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `RHLLMChatNode` —— 2/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `MultiTextConcatenate` —— 1/6 个有
- `RebelsKrea2OutpaintCanvas` —— 1/6 个有
- `RebelsKrea2OutpaintComposite` —— 1/6 个有
- `RebelsKrea2OutpaintEncode` —— 1/6 个有
- `RebelsKrea2OutpaintModelPatch` —— 1/6 个有
- `SaveImageAdvanced` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
