---
name: text_to_image_lora_sampler_clip_163
type: Text To Image
frequency: 7
level: strong
coverage: 0.900429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json, 图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json, 图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102097450449326081.json, 图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json, 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE工作流，文生图高质量文本到图像_2107569921352884226.json, 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen2.1双图组合｜两张图片智能融合风格化，千问2.1图生图玩法_2107293954797555714.json、图片生成/图生图/Qwen2.1透明抠图｜一键抠出透明背景素材，电商设计抠图必备神器_2107290862001680386.json、图片生成/文生图/Image-2.5图片编辑极速版 全能图片G2.5快速处理_2098306932686802946.json、图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102097450449326081.json、图片生成/文生图/Qwen Image 2.1文生图标准版｜一句话生成好图｜写实插画都能驾驭_2102638633646907393.json…）

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
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 6/7 个有
- `ResolutionSelector` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `BasicGuider` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `QwenImage21FunPDDLoader` —— 2/7 个有
- `RandomNoise` —— 2/7 个有
- `SamplerCustomAdvanced` —— 2/7 个有
- `PixaromaRunTimer` —— 1/7 个有
- `PixaromaSeed` —— 1/7 个有
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 1/7 个有

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
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
