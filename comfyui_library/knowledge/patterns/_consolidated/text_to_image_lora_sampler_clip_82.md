---
name: text_to_image_lora_sampler_clip_82
type: Text To Image
frequency: 15
level: weak
coverage: 0.648667
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, GetNode, KSampler, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader, YUAN_TXTConvertAny, YUAN_TXTParagraphSplitter]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2短剧拍档｜场景角色文生图分镜出图_2089429856026189826.json, 图片生成/文生图/云信漫剧短剧资产生成系统_2086736400015253506.json, 图片生成/文生图/短剧场景角色资产｜Krea2文生图一键生成_2089808604294635522.json, 图片生成/文生图/短剧拍档V9.0｜Krea2场景角色文生图支持_2089835303707176961.json, 图片生成/文生图/短剧拍档场景角色生成｜Krea2版文生图工作流_2093811071009255426.json, 图片生成/文生图/短剧拍档支持场景和角色V7(Krea2版)_2079196390848286721.json, 图片生成/文生图/短剧拍档支持场景和角色V8.0(Krea2版)_2084946322783825922.json, 图片生成/文生图/短剧角色场景道具多合一｜傲雪AIGC MiniMax H3工作流_2093767569130999810.json, 图片生成/文生图/资产生成短剧拍档V16.1 Qwen2.1可编辑版，文生图图生图短剧资产工具_2106108165623468034.json, 音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json, 音频生成/音频生成/场景角色双支持｜短剧拍档V12.2继承版资产生成_2091795341573181442.json, 音频生成/音频生成/短剧拍档V12.1重置版｜资产生成文生图音频_2092888610189176834.json, 音频生成/音频生成/短剧拍档V13.1预览编辑版 资产生成与角色管理_2098292808837849090.json, 音频生成/音频生成/短剧拍档V13.1预览编辑版 资产生成与角色管理工具_2098705139308777473.json, 音频生成/音频生成/短剧拍档资产生成｜V12.1重置版文生图音频_2091793261215178753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Krea2短剧拍档｜场景角色文生图分镜出图_2089429856026189826.json、图片生成/文生图/云信漫剧短剧资产生成系统_2086736400015253506.json、图片生成/文生图/短剧场景角色资产｜Krea2文生图一键生成_2089808604294635522.json、图片生成/文生图/短剧拍档V9.0｜Krea2场景角色文生图支持_2089835303707176961.json、图片生成/文生图/短剧拍档场景角色生成｜Krea2版文生图工作流_2093811071009255426.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `YUAN_TXTParagraphSplitter`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 13/15 个有
- `Fast Groups Bypasser (rgthree)` —— 13/15 个有
- `KSamplerSelect` —— 13/15 个有
- `PrimitiveBoolean` —— 13/15 个有
- `RandomNoise` —— 13/15 个有
- `SamplerCustomAdvanced` —— 13/15 个有
- `JjkText` —— 12/15 个有
- `YUAN_TXTJsonExtractor` —— 12/15 个有
- `solarL_SaveImagesToZip` —— 12/15 个有
- `孤海注释` —— 12/15 个有
- `CFGGuider` —— 11/15 个有
- `ShowText|pysssss` —— 11/15 个有
- `ComfyMathExpression` —— 8/15 个有
- `FB_Qwen3TTSVoiceDesign` —— 8/15 个有
- `SaveAudio` —— 8/15 个有
- `StringConcatenate` —— 8/15 个有
- `StringReplace` —— 8/15 个有
- `easy positive` —— 7/15 个有
- `LoadImage` —— 6/15 个有
- `YUAN_TXTReplace` —— 6/15 个有
- `VAEEncode` —— 5/15 个有
- `BasicGuider` —— 4/15 个有
- `YUAN_TXTPreviewContent` —— 4/15 个有
- `ModelPatchLoader` —— 3/15 个有
- `ZImageFunControlnet` —— 3/15 个有
- `CLIPLoaderGGUF` —— 2/15 个有
- `CustomCombo` —— 2/15 个有
- `Image Comparer (rgthree)` —— 2/15 个有
- `PreviewAny` —— 2/15 个有
- `ResolutionSelector` —— 2/15 个有
- `TextEncodeQwenImage21` —— 2/15 个有
- `YuanCustomCombo` —— 2/15 个有
- `ClipLoaderGGUF` —— 1/15 个有
- `PreviewImage` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 15 | 0% |
| 高度 | 80 | 80 - 1920 | 15 | 0% |
| 采样步数 | 4 | 4 - 8 | 15 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 63% |
| 采样算法 | er_sde | - | 15 | 80% |
| 调度器 | beta | - | 15 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，15 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 80%
- 调度器 最常用 beta，15 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
