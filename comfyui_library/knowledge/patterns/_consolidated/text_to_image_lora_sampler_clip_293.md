---
name: text_to_image_lora_sampler_clip_293
type: Text To Image
frequency: 7
level: strong
coverage: 0.881571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1一键图片自动透明分层，精准抠图图层分离图生图工具_2103258930473422849.json, 图片生成/图生图/Qwen Image 2.1一键抠图PNG通道输出，透明背景图生图工具_2102886783691354114.json, 图片生成/图生图/Qwen Image 2.1双图参考编辑｜图生图换背景与图片处理一步到位_2104481950252756993.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102506921529004033.json, 图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工作流_2102089735173926914.json, 图片生成/图生图/千问2.1双图参考编辑 两张输入精准改图_2104672253739880450.json, 图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_293

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1一键图片自动透明分层，精准抠图图层分离图生图工具_2103258930473422849.json、图片生成/图生图/Qwen Image 2.1一键抠图PNG通道输出，透明背景图生图工具_2102886783691354114.json、图片生成/图生图/Qwen Image 2.1双图参考编辑｜图生图换背景与图片处理一步到位_2104481950252756993.json、图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102506921529004033.json、图片生成/图生图/Qwen Image 2.1多图编辑文生图图生图处理工作流_2102089735173926914.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `PreviewAny` —— 3/7 个有
- `SaveImageAdvanced` —— 3/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `ModelAttentionBackend` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `RHLLMChatNode` —— 1/7 个有
- `Text Load Line From File` —— 1/7 个有
- `easy forLoopEnd` —— 1/7 个有
- `easy forLoopStart` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
