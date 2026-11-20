---
name: text_to_image_lora_sampler_clip_112
type: Text To Image
frequency: 13
level: weak
coverage: 0.647385
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, GetNode, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RegexExtract, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTParagraphSplitter]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2短剧拍档｜场景角色文生图分镜出图_2089429856026189826.json, 图片生成/文生图/云信漫剧短剧资产生成系统_2086736400015253506.json, 图片生成/文生图/短剧场景角色资产｜Krea2文生图一键生成_2089808604294635522.json, 图片生成/文生图/短剧拍档V9.0｜Krea2场景角色文生图支持_2089835303707176961.json, 图片生成/文生图/短剧拍档场景角色生成｜Krea2版文生图工作流_2093811071009255426.json, 图片生成/文生图/短剧拍档支持场景和角色V7(Krea2版)_2079196390848286721.json, 图片生成/文生图/短剧拍档支持场景和角色V8.0(Krea2版)_2084946322783825922.json, 图片生成/文生图/短剧角色场景道具多合一｜傲雪AIGC MiniMax H3工作流_2093767569130999810.json, 音频生成/音频生成/场景角色双支持｜短剧拍档V12.2继承版资产生成_2091795341573181442.json, 音频生成/音频生成/短剧拍档V12.1重置版｜资产生成文生图音频_2092888610189176834.json, 音频生成/音频生成/短剧拍档V13.1预览编辑版 资产生成与角色管理_2098292808837849090.json, 音频生成/音频生成/短剧拍档V13.1预览编辑版 资产生成与角色管理工具_2098705139308777473.json, 音频生成/音频生成/短剧拍档资产生成｜V12.1重置版文生图音频_2091793261215178753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Krea2短剧拍档｜场景角色文生图分镜出图_2089429856026189826.json、图片生成/文生图/云信漫剧短剧资产生成系统_2086736400015253506.json、图片生成/文生图/短剧场景角色资产｜Krea2文生图一键生成_2089808604294635522.json、图片生成/文生图/短剧拍档V9.0｜Krea2场景角色文生图支持_2089835303707176961.json、图片生成/文生图/短剧拍档场景角色生成｜Krea2版文生图工作流_2093811071009255426.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RegexExtract`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `YUAN_TXTParagraphSplitter`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 11/13 个有
- `ShowText|pysssss` —— 11/13 个有
- `JjkText` —— 10/13 个有
- `YUAN_TXTJsonExtractor` —— 10/13 个有
- `solarL_SaveImagesToZip` —— 10/13 个有
- `孤海注释` —— 10/13 个有
- `easy positive` —— 7/13 个有
- `ComfyMathExpression` —— 6/13 个有
- `FB_Qwen3TTSVoiceDesign` —— 6/13 个有
- `SaveAudio` —— 6/13 个有
- `StringConcatenate` —— 6/13 个有
- `StringReplace` —— 6/13 个有
- `BasicGuider` —— 4/13 个有
- `LoadImage` —— 4/13 个有
- `YUAN_TXTReplace` —— 4/13 个有
- `ModelPatchLoader` —— 3/13 个有
- `VAEEncode` —— 3/13 个有
- `ZImageFunControlnet` —— 3/13 个有
- `CLIPLoaderGGUF` —— 2/13 个有
- `CustomCombo` —— 2/13 个有
- `Image Comparer (rgthree)` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `YUAN_TXTPreviewContent` —— 2/13 个有
- `ClipLoaderGGUF` —— 1/13 个有
- `PreviewImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 13 | 0% |
| 高度 | 80 | 80 - 1920 | 13 | 0% |
| 采样步数 | 4 | 4 - 8 | 13 | 66% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 60% |
| 采样算法 | er_sde | - | 13 | 77% |
| 调度器 | beta | - | 13 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，13 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 77%
- 调度器 最常用 beta，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
