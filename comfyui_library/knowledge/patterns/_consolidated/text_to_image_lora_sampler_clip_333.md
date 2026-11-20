---
name: text_to_image_lora_sampler_clip_333
type: Text To Image
frequency: 6
level: strong
coverage: 0.898167
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1双图编辑 两张参考图图生图处理工具_2113021920923971585.json, 图片生成/图生图/Qwen image 2.1图片编辑二号版｜图生图精细修改随心改_2112816409389649921.json, 图片生成/图生图/Qwen image2.1单图编辑｜图片换背景轻松搞定｜模特产品展示利器_2102227263780642818.json, 图片生成/图生图/Qwen image2.1多图编辑实用版｜多张图片统一处理｜其它图片处理通吃_2102216509333528578.json, 图片生成/图生图/Qwen_image2.1单图编辑｜图片换背景轻松搞定｜模特产品展示利器_2104449836132159489.json, 图片生成/图生图/Qwen_image2.1多图编辑实用版｜多张图片统一处理｜其它图片处理通吃_2102321477453443073.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_333

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1双图编辑 两张参考图图生图处理工具_2113021920923971585.json、图片生成/图生图/Qwen image 2.1图片编辑二号版｜图生图精细修改随心改_2112816409389649921.json、图片生成/图生图/Qwen image2.1单图编辑｜图片换背景轻松搞定｜模特产品展示利器_2102227263780642818.json、图片生成/图生图/Qwen image2.1多图编辑实用版｜多张图片统一处理｜其它图片处理通吃_2102216509333528578.json、图片生成/图生图/Qwen_image2.1单图编辑｜图片换背景轻松搞定｜模特产品展示利器_2104449836132159489.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/6 个有
- `RHLLMChatNode` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `QwenPERewriteT8` —— 2/6 个有
- `ResizeLongestToNode` —— 2/6 个有
- `PrimitiveString` —— 1/6 个有
- `StringToInt` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
