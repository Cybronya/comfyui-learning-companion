---
name: text_to_image_lora_sampler_clip_235
type: Text To Image
frequency: 8
level: weak
coverage: 0.872
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen 3.5反推图片提示词（llama反推高速版）_2071872448303292417.json, 图片生成/反推提示词/qwen3.8-27B反推图片提示词｜反推提示词神器 一句话还原图片描述_2104032262567321602.json, 图片生成/反推提示词/千问3.5大语言模型｜反推提示词支持9图同时解析_2110697516319723521.json, 图片生成/反推提示词/千问qwen3.5图片反推提示词｜看图自动写出文本描述_2103054712437305346.json, 图片生成/图生图/Flux3-klein指定位置修改，局部重绘图生图方案_2111947609521868801.json, 图片生成/图生图/Flux3_klein图像编辑，图生图动作迁移数字人微调样样通_2112681484900462593.json, 图片生成/图生图/flux3_klein 图片编辑｜写实美少女修图利器_2112443453094318082.json, 图片生成/图生图/flux3_klein图片编辑，美少女写实风图生图微调_2112632993977294850.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_235

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Qwen 3.5反推图片提示词（llama反推高速版）_2071872448303292417.json、图片生成/反推提示词/qwen3.8-27B反推图片提示词｜反推提示词神器 一句话还原图片描述_2104032262567321602.json、图片生成/反推提示词/千问3.5大语言模型｜反推提示词支持9图同时解析_2110697516319723521.json、图片生成/反推提示词/千问qwen3.5图片反推提示词｜看图自动写出文本描述_2103054712437305346.json、图片生成/图生图/Flux3-klein指定位置修改，局部重绘图生图方案_2111947609521868801.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `solarL_SaveImagesToZip` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `SaveImage` —— 6/8 个有
- `BatchImagesNode` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `ReferenceMultiLatent` —— 4/8 个有
- `TextGenerate` —— 4/8 个有
- `llama_cpp_instruct_adv` —— 4/8 个有
- `llama_cpp_model_loader` —— 4/8 个有
- `EmptyFlux2LatentImage` —— 3/8 个有
- `easy saveText` —— 3/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `ResolutionSelector` —— 2/8 个有
- `Text` —— 2/8 个有
- `llama_cpp_parameters` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Ideogram4PromptBuilderKJ` —— 1/8 个有
- `PreviewImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 8 | 0% |
| 高度 | 80 | 80 - 1920 | 8 | 0% |
| 采样步数 | 4 | 4 - 8 | 8 | 71% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 72% |
| 采样算法 | er_sde | - | 8 | 88% |
| 调度器 | beta | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，8 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本
- 采样算法 最常用 er_sde，8 个样本，一致性 88%
- 调度器 最常用 beta，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
