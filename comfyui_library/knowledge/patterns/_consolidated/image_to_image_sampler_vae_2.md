---
name: image_to_image_sampler_vae_2
type: Image To Image
frequency: 35
level: strong
coverage: 0.782343
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/42. 专业级证件照生成，参数区输入证件照模版和处理图片+背景+服装+领带，即可出单张和9张图片_1974772408315940866.json, 图片生成/图生图/QWEN快速换装秒出图_1985441625268699137.json, 图片生成/图生图/Qwen image edit plus和自己相拥_1970442909982093313.json, 图片生成/图生图/Qwen去水印+高清处理_2011600241761456129.json, 图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1971470726085722113.json, 图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1977867242929016833.json, 图片生成/图生图/一键去水印高清修复版千问qwen图片编辑2509快速去水印图片去水印加速版_2061066797192933377.json, 图片生成/图生图/一键图片去水印加高清修复_1999007653064007682.json, 图片生成/图生图/人物换衣服_2095498989033578497.json, 图片生成/图生图/人物换衣服加速版qwen edit plus+全节点注释_2055626898692157442.json, 图片生成/图生图/人物换衣服加速版qwen+edit+plus+全节点注释_2060616197187657729.json, 图片生成/图生图/人物换衣服加速版qwen+edit+plus+全节点注释_2114881435655041026.json, 图片生成/图生图/去水印  高清修复_1989266952667492353.json, 图片生成/图生图/去水印  高清修复_2007447402684358657.json, 图片生成/图生图/衣服提取提取衣服（加速版）qweneditplus_1971448005004083201.json, 图片生成/图生图/衣服提取提取衣服（加速版）qweneditplus_2041345450657193986.json, 图片生成/图生图/（单图推荐）tele style画风迁移，游戏_动漫角色设计_2054939690477858817.json, 图片生成/图生图/👾怪獸-千问多图编辑8步版👾_1977240342351237121.json, 图片生成/文生图/人物换衣服加速版qwen edit plus+全节点注释_2055669100139040769.json, 图片生成/文生图/千问 手办盲盒超火模型_1993973079732846594.json, 平台全量/Qwen极速换装 换脸 换头 人物换衣服加速版 edit plus_2055159492337250305.json, 平台全量/【极速换装】Qwen-edit电商级OOTE辣妹模特换装 换装人物换装加速版_1976923204184903682.json, 平台全量/一键去水印（高清修复版）_2009254507045199874.json, 平台全量/一键图片去水印+图片高清修复 洗图去除水印_2028653424912371714.json, 平台全量/人物换衣服加速版qwen+edit+plus_2061597336681406465.json, 平台全量/人物换装换脸 服饰提取 人物精准换装 加速版  SeedVR2.5 + TTP 分块高清放大_2013510838342131714.json, 平台全量/动漫角色动态生图_2011367524272705537.json, 平台全量/去水印加高清修复_qwen_1987020658632798209.json, 平台全量/手办盲盒超火模型_1970460823921565697.json, 平台全量/手办盲盒超火模型_2033803692750675969.json, 平台全量/手办盲盒超火模型_2044942277717532673.json, 平台全量/手办盲盒超火模型图片转3D手办模型_1970816569913843714.json, 平台全量/换装人物换装加速版qweneditplus_1971450322667388929.json, 平台全量/极速换装 换脸 换头 人物换衣服加速版qwen edit plus_2055109425047842818.json, 平台全量/水印去除加速版v2_1970441135615320066.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 35 个 workflow 归纳得出（图片生成/图生图/42. 专业级证件照生成，参数区输入证件照模版和处理图片+背景+服装+领带，即可出单张和9张图片_1974772408315940866.json、图片生成/图生图/QWEN快速换装秒出图_1985441625268699137.json、图片生成/图生图/Qwen image edit plus和自己相拥_1970442909982093313.json、图片生成/图生图/Qwen去水印+高清处理_2011600241761456129.json、图片生成/图生图/qwen千问多图编辑4步_双节棍nunchaku加速版本_1971470726085722113.json…）

- **类型**：Image To Image
- **样本数**：35
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 35 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 34/35 个有
- `ConditioningZeroOut` —— 33/35 个有
- `LoraLoaderModelOnly` —— 33/35 个有
- `PrimitiveStringMultiline` —— 33/35 个有
- `UNETLoader` —— 33/35 个有
- `CR Simple Image Compare` —— 28/35 个有
- `easy imageConcat` —— 13/35 个有
- `PathchSageAttentionKJ` —— 5/35 个有
- `ImageConcatMulti` —— 4/35 个有
- `DWPreprocessor` —— 2/35 个有
- `NunchakuQwenImageDiTLoader` —— 2/35 个有
- `PrimitiveString` —— 1/35 个有
- `RBGImageStitchPlus` —— 1/35 个有
- `RHHiddenNodes` —— 1/35 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 35 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 35 | 100% |
| 采样算法 | euler | - | 35 | 100% |
| 调度器 | simple | - | 35 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 35 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/35 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/35 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，35 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，35 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，35 个样本，一致性 100%
- 调度器 最常用 simple，35 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，35 个样本，取值集中（一致性 100%）
- 高发问题（35/35 个样本）：Steps较低可能导致细节不足
