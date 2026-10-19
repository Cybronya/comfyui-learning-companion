---
name: text_to_image_lora_sampler_clip_130
type: Text To Image
frequency: 7
level: strong
coverage: 0.899571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Topaz星光高清放大模型｜数毛党最爱地表最强，视频超分拉满_2107366759350235137.json, 图片生成/文生图/Krea2 Trubo极速文生图｜美商极高出图快 颜值党直呼内行_2105557272117202946.json, 图片生成/文生图/Krea2 Turbo极速版美商极高文生图V2_2100289687335297026.json, 图片生成/文生图/Krea2 Turbo极速版美商极高文生图，高质量文本到图像生成工具_2105735805019971585.json, 图片生成/文生图/Qwen2.1文生图写实风格 照片级质感画面直出_2105475614315737089.json, 图片生成/文生图/千问qwen image 2.1文生图工作流 高质量画面直出_2104994907697012737.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜注意仅供学习不可商用_2104770730121588737.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Topaz星光高清放大模型｜数毛党最爱地表最强，视频超分拉满_2107366759350235137.json、图片生成/文生图/Krea2 Trubo极速文生图｜美商极高出图快 颜值党直呼内行_2105557272117202946.json、图片生成/文生图/Krea2 Turbo极速版美商极高文生图V2_2100289687335297026.json、图片生成/文生图/Krea2 Turbo极速版美商极高文生图，高质量文本到图像生成工具_2105735805019971585.json、图片生成/文生图/Qwen2.1文生图写实风格 照片级质感画面直出_2105475614315737089.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `QZ_ResolutionPreset` —— 3/7 个有
- `LoadVideo` —— 1/7 个有
- `RH_Astra` —— 1/7 个有
- `RunningHub Deepcleaner` —— 1/7 个有
- `SaveVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
