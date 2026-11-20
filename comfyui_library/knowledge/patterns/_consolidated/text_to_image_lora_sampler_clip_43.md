---
name: text_to_image_lora_sampler_clip_43
type: Text To Image
frequency: 20
level: weak
coverage: 0.89745
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-双采大胸版_2089250736138964993.json, 图片生成/文生图/Krea2-模糊感美女生成_2091102588728074241.json, 图片生成/文生图/Krea2-百变美女2_2094969323881320450.json, 图片生成/文生图/Krea2-百变美女_2093983095182684161.json, 图片生成/文生图/Krea2-美女生成双采_2088668185955491842.json, 图片生成/文生图/Krea2-美女生成语义增强版_2089887983045533698.json, 图片生成/文生图/Krea2模糊感美女生成｜文生图一键直出创作_2091289552974598145.json, 图片生成/文生图/Krea2美女生成双采｜文生图高清直出创作_2091314568529276929.json, 图片生成/文生图/Krea2美女生成语义增强版｜文生图一键生成直出_2091315805886697473.json, 图片生成/文生图/MOSS_Image_SFT_BF16+4步加速LoRA文生图｜美少女写实出图快_2114248990190559233.json, 图片生成/文生图/Moss Base文生图基础版 基础模式图像生成处理工具_2113776137825513473.json, 图片生成/文生图/Moss SFT Fixed文生图 修正版高质量图像生成工具_2113722107573129217.json, 图片生成/文生图/Moss SFT文生图极简版 极简模式高质量生成工具_2113777659305095170.json, 图片生成/文生图/Moss Sft Fixed文生图｜SFT微调模型稳定文生图体验_2113592740046000130.json, 图片生成/文生图/Qwen Image 2.1文生图增强版照片级写实创意插画商业宣传物料概念设计_2108659062555635713.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102097450449326081.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2105772682397700098.json, 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE工作流，文生图高质量文本到图像_2107569921352884226.json, 图片生成/文生图/Qwen image 2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2102246172638408706.json, 图片生成/文生图/Qwen image 2.1文生图角色四视图V1.1 角色设定批量产出_2109347086192963585.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Krea2-双采大胸版_2089250736138964993.json、图片生成/文生图/Krea2-模糊感美女生成_2091102588728074241.json、图片生成/文生图/Krea2-百变美女2_2094969323881320450.json、图片生成/文生图/Krea2-百变美女_2093983095182684161.json、图片生成/文生图/Krea2-美女生成双采_2088668185955491842.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 15/20 个有
- `JjkText` —— 14/20 个有
- `solarL_SaveImagesToZip` —— 14/20 个有
- `孤海注释` —— 14/20 个有
- `PrimitiveBoolean` —— 10/20 个有
- `ResolutionSelector` —— 10/20 个有
- `LatentUpscaleBy` —— 9/20 个有
- `Switch string [Crystools]` —— 9/20 个有
- `TextEncodeQwenImage21` —— 6/20 个有
- `EmptyFlux2LatentImage` —— 5/20 个有
- `TextGenerateLTX2Prompt` —— 4/20 个有
- `StringConcatenate` —— 3/20 个有
- `easy showAnything` —— 3/20 个有
- `ConditioningRebalanceKrea2` —— 2/20 个有
- `KSamplerAdvanced` —— 2/20 个有
- `ComfySwitchNode` —— 1/20 个有
- `SaveImageAdvanced` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 19 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 2.5 - 8 | 20 | 71% |
| 采样算法 | er_sde | - | 20 | 70% |
| 调度器 | beta | - | 20 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 1024 | 20 | 0% |
| 高度 | 80 | 80 - 1536 | 20 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，19 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 2.5 - 8，20 个样本
- 采样算法 最常用 er_sde，20 个样本，一致性 70%
- 调度器 最常用 beta，20 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，20 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，20 个样本，取值分散，一致性仅 0%
- 高发问题（31/20 个样本）：Steps较低可能导致细节不足
