---
name: text_to_image_lora_sampler_clip_126
type: Text To Image
frequency: 12
level: strong
coverage: 0.891417
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Outpaint LoRA图像扩图目前最佳｜Krea2图生图扩图工作流_2087211988345769985.json, 图片生成/图生图/Qwen Image 2.1图生图工作流，人像写真风格化图生图处理方案_2106885969646542849.json, 图片生成/图生图/Qwen Image 2.1多参考图生图｜标准版稳定出图首选_2105137018840899585.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102105087035400194.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102483334352953345.json, 图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102506921529004033.json, 图片生成/图生图/Qwen Image 2.1文生图图生图处理生成工作流_2102101983669866498.json, 图片生成/图生图/Qwen Image 2.1生图及编辑工作流，支持12张参考图一致性最强开源方案_2107154350245240833.json, 图片生成/图生图/Qwen Image 2.1精准抠图工作流，指哪扣哪的交互式图生图体验_2102816199997480961.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，支持三视图参考的图生图工作流_2102897765192916994.json, 图片生成/图生图/Qwen image 2.1图像编辑通用版｜图生图指令改图｜听懂人话好上手_2102285690850598914.json, 图片生成/图生图/Qwen image 2.1图片编辑｜图生图改图如此简单 指哪改哪_2105534138802593793.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Outpaint LoRA图像扩图目前最佳｜Krea2图生图扩图工作流_2087211988345769985.json、图片生成/图生图/Qwen Image 2.1图生图工作流，人像写真风格化图生图处理方案_2106885969646542849.json、图片生成/图生图/Qwen Image 2.1多参考图生图｜标准版稳定出图首选_2105137018840899585.json、图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102105087035400194.json、图片生成/图生图/Qwen Image 2.1多图编辑图生图处理生成工具_2102483334352953345.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
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
- `TextEncodeQwenImage21` —— 11/12 个有
- `QwenImage21Cache` —— 10/12 个有
- `ComfySwitchNode` —— 9/12 个有
- `ResolutionSelector` —— 9/12 个有
- `SaveImageAdvanced` —— 7/12 个有
- `CR Text` —— 4/12 个有
- `CR Prompt Text` —— 1/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `QwenPERewriteT8` —— 1/12 个有
- `RHLLMChatNode` —— 1/12 个有
- `RebelsKrea2OutpaintCanvas` —— 1/12 个有
- `RebelsKrea2OutpaintComposite` —— 1/12 个有
- `RebelsKrea2OutpaintEncode` —— 1/12 个有
- `RebelsKrea2OutpaintModelPatch` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
