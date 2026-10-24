---
name: image_to_image_lora_sampler_unet_7
type: Image To Image
frequency: 38
level: strong
coverage: 0.590974
common_nodes: [CFGNorm, CLIPLoader, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Extract_Clothing_Person_QwenEdit2511_JAMES001_2079604027645583362.json, 图片生成/图生图/Qwen Image Edit 2511-带F2P-支持单图多图编辑_2046849881221898241.json, 图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2069233419581739009.json, 图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2074649896665305089.json, 图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2082990309067284481.json, 图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2083017932996698114.json, 图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2083110808443252737.json, 图片生成/图生图/Qwen2511一键提取衣服+分离人物_2058472808627392513.json, 图片生成/图生图/Qwen2511一键提取衣服+分离人物_2058477521829711874.json, 图片生成/图生图/一张图片一键生成多角度多镜头 短剧必备_2016515954150215681.json, 图片生成/图生图/一张图片一键生成多角度多镜头 短剧必备_2091722800968065026.json, 图片生成/图生图/一键去壳！提取衣服分离人物-QwenEdit2511_2008516971700162561.json, 图片生成/图生图/一键提取衣服+分离人物+QwenEdit2511_2049018174875639810.json, 图片生成/图生图/一键提取衣服+分离人物=QwenEdit2511_2005532150214656002.json, 图片生成/图生图/一键提取衣服+分离人物=QwenEdit2511_2029572534571634689.json, 图片生成/图生图/一键提取衣服+分离人物=QwenEdit2511_2085666548760535042.json, 图片生成/图生图/一键提取衣服+分离人物=QwenEdit2511_2097881619569922050.json, 图片生成/图生图/一键提取衣服+分离人物=QwenEdit2511_2099411845491814402.json, 图片生成/图生图/一键提取衣服+分离人物（电商专用）_2045054734444273665.json, 图片生成/图生图/一键提服饰搭配+分离人物_2053484068637028354.json, 图片生成/图生图/一键生成多图多镜头+多角度=Qwen-Multiple-angles_2069247378271592449.json, 图片生成/图生图/一键生成多角度_多视角美女_2010711715217936385.json, 图片生成/图生图/一键生成多镜头+多角度2_2098938629342187522.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles_1984963830654648321.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles_2042955576895873025.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles。好用到爆，超乎你想象！_2031902890029223937.json, 图片生成/图生图/一键生成多镜头+多角度=Qwen-Multiple-angles。好用到爆，超乎你想象！_2041156746311376898.json, 图片生成/图生图/一键生成多镜头+多角度_1997597737426292738.json, 图片生成/图生图/一键生成多镜头+多角度_2012761833446318081.json, 图片生成/图生图/一键生成多镜头+多角度_2019406910067318785.json, 图片生成/图生图/一键生成多镜头+多角度_2020848993571446785.json, 图片生成/图生图/一键生成多镜头+多角度_2069941228808003585.json, 图片生成/图生图/人物多机位视角切换_2009853282759483393.json, 图片生成/图生图/千问Qwen edit 2509BF16原版 图片一键生成多角度、多镜头控制工作流_1986296620218286081.json, 图片生成/图生图/图片多机位切换_1993495709802577921.json, 图片生成/图生图/提取人物衣服+分离人物 生成白底 QwenEdit_2087017832470106114.json, 图片生成/图生图/穿搭博主福音（一键拆分人物与服装）QwenEdit2511_2028285007155957762.json, 视频生成/图生视频/一键提取衣服+分离人物（懒人版上传就行）_2066580683623063553.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 38 个 workflow 归纳得出（图片生成/图生图/Extract_Clothing_Person_QwenEdit2511_JAMES001_2079604027645583362.json、图片生成/图生图/Qwen Image Edit 2511-带F2P-支持单图多图编辑_2046849881221898241.json、图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2069233419581739009.json、图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2074649896665305089.json、图片生成/图生图/Qwen-Multiple-angl一键生成多镜头+多角度_2082990309067284481.json…）

- **类型**：Image To Image
- **样本数**：38
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 38 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 37/38 个有
- `LayerUtility: PurgeVRAM` —— 37/38 个有
- `PrimitiveInt` —— 37/38 个有
- `GetNode` —— 22/38 个有
- `SetNode` —— 22/38 个有
- `ImageConcatMulti` —— 20/38 个有
- `EmptySD3LatentImage` —— 16/38 个有
- `FluxKontextMultiReferenceLatentMethod` —— 16/38 个有
- `easy imageConcat` —— 15/38 个有
- `ImageStitch` —— 14/38 个有
- `PreviewImage` —— 3/38 个有
- `Fast Groups Muter (rgthree)` —— 2/38 个有
- `Image Comparer (rgthree)` —— 1/38 个有
- `Int` —— 1/38 个有
- `Text` —— 1/38 个有
- `孤海注释` —— 1/38 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 38 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 38 | 100% |
| 采样算法 | euler | - | 38 | 100% |
| 调度器 | simple | - | 38 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 38 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 211/38 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，38 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，38 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，38 个样本，一致性 100%
- 调度器 最常用 simple，38 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，38 个样本，取值集中（一致性 100%）
- 高发问题（211/38 个样本）：Steps较低可能导致细节不足
