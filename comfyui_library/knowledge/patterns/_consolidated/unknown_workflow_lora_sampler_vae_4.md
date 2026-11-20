---
name: unknown_workflow_lora_sampler_vae_4
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.898538
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Eidt-2511-Simple三图参考图生图.json_2057396945701924866.json, 图片生成/图生图/qwen2511单手美甲迁移_1977666067403366401.json, 图片生成/图生图/qwen2511去除ai感_2013073387723165697.json, 图片生成/图生图/qwen2511图案提取_1996890196249571329.json, 图片生成/图生图/一键多图千问改图2511_2005940642993893377.json, 图片生成/图生图/三图参考合成新图 智能描述快速合成_2039164588914118657.json, 图片生成/图生图/三图参考图生图-邻家AI大女孩_2043619272265568257.json, 图片生成/图生图/升级版三图合成新图V2_2006167893603520514.json, 图片生成/图生图/图生图 三图参考人物一致性 智能描述极速版_2010646379785363457.json, 图片生成/图生图/图生图(3图参考)-分镜图-Qwen-Eidt+SeedVR_2052204516816236546.json, 图片生成/图生图/图生图(3图参考)-分镜图-Qwen-Eidt+SeedVR_2062450638046449665.json, 图片生成/图生图/恶搞神器-三图生神图-Qwen-Eidt-2511+SeedVR_2031255189180649474.json, 图片生成/图生图/皮雕一键生成_2060225712279343106.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen-Eidt-2511-Simple三图参考图生图.json_2057396945701924866.json、图片生成/图生图/qwen2511单手美甲迁移_1977666067403366401.json、图片生成/图生图/qwen2511去除ai感_2013073387723165697.json、图片生成/图生图/qwen2511图案提取_1996890196249571329.json、图片生成/图生图/一键多图千问改图2511_2005940642993893377.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `ImageConcanate` —— 11/13 个有
- `PreviewImage` —— 11/13 个有
- `SeedVR2LoadDiTModel` —— 9/13 个有
- `SeedVR2LoadVAEModel` —— 9/13 个有
- `SeedVR2VideoUpscaler` —— 9/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `Fast Groups Muter (rgthree)` —— 8/13 个有
- `ImageConcatMulti` —— 7/13 个有
- `Int` —— 1/13 个有
- `UnetLoaderGGUF` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 720 | 720 - 1280 | 13 | 76% |
| 高度 | 1280 | 720 - 1280 | 13 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 720 - 1280，13 个样本
- 高度 中位数 1280，观测区间 720 - 1280，13 个样本，取值集中（一致性 83%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
