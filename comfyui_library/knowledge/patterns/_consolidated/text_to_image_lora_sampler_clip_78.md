---
name: text_to_image_lora_sampler_clip_78
type: Text To Image
frequency: 15
level: moderate
coverage: 0.8978
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1单图编辑工作流，风格化图生图单图编辑处理工具_2107594764458745858.json, 图片生成/图生图/Qwen2.1双图组合工作流，风格化图生图双图融合处理工具_2107593203762417666.json, 图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json, 图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2109523834180292610.json, 图片生成/图生图/Qwen2.1透明抠图工作流，图生图抠图背景移除处理工具_2107591647239426050.json, 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json, 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2109524566442856449.json, 图片生成/图生图/Qwen_Image_2.1一键抠图PNG通道输出，透明背景图生图工具_2105110544796708866.json, 图片生成/图生图/Qwen_Image_2.1精准抠图工作流，指哪扣哪的交互式图生图体验_2106553795676303362.json, 图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，图生图快速产出故事板_2105851031333728258.json, 图片生成/图生图/Qwen_Image_2.1自动分镜短剧分镜生成，支持三视图参考的图生图工作流_2104738814660014082.json, 图片生成/图生图/qwen-image-2.1一键抠图｜PNG透明通道直出｜抠图发丝级细节保留_2102320037234302977.json, 图片生成/图生图/（6图编辑）QwenImage2.1 turbo专用工作流 高效改图方案_2111592341713801218.json, 图片生成/文生图/Qwen-image 2.1 Turbo文生图，图生图高效出片_2110863379169636354.json, 图片生成/文生图/QwenImage2.1 turbo专用工作流 高效改图方案_2109710779971891202.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_78

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Qwen2.1单图编辑工作流，风格化图生图单图编辑处理工具_2107594764458745858.json、图片生成/图生图/Qwen2.1双图组合工作流，风格化图生图双图融合处理工具_2107593203762417666.json、图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json、图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2109523834180292610.json、图片生成/图生图/Qwen2.1透明抠图工作流，图生图抠图背景移除处理工具_2107591647239426050.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 10/15 个有
- `RandomNoise` —— 10/15 个有
- `SamplerCustomAdvanced` —— 10/15 个有
- `QwenImage21Cache` —— 8/15 个有
- `EmptyImage` —— 7/15 个有
- `PreviewImage` —— 7/15 个有
- `QwenImage21FunPDDLoader` —— 7/15 个有
- `孤海注释` —— 7/15 个有
- `ComfySwitchNode` —— 6/15 个有
- `PrimitiveInt` —— 6/15 个有
- `PrimitiveStringMultiline` —— 5/15 个有
- `ResolutionSelector` —— 5/15 个有
- `SaveImageAdvanced` —— 5/15 个有
- `Fast Groups Bypasser (rgthree)` —— 3/15 个有
- `KSamplerSelect` —— 3/15 个有
- `ManualSigmas` —— 3/15 个有
- `PrimitiveBoolean` —— 3/15 个有
- `CR Text` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 1024 | 15 | 0% |
| 高度 | 80 | 80 - 1024 | 15 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
