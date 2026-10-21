---
name: text_to_image_sampler_clip_vae_16
type: Text To Image
frequency: 4
level: strong
coverage: 0.8385
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, CR Text Replace, EmptyLatentImage, JDCN_StringToList, KSampler, ModelSamplingAuraFlow, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, Seed (rgthree), Text Concatenate, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image： 原版⚡️BEYOND REALITY⚡️红潮黑兽⚡️三种模型文生图对比_2006969820541100033.json, 图片生成/文生图/（量贩版）Qwen 2512 Kook真实版极速自动扩写文生图V1_2008588511217192962.json, 图片生成/文生图/（量贩版）Qwen Image 2512极速自动扩写文生图 多图多风格_2007703405346689025.json, 图片生成/文生图/（量贩版）Qwen Image 2512极速自动扩写文生图V1_2006361347503693825.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image： 原版⚡️BEYOND REALITY⚡️红潮黑兽⚡️三种模型文生图对比_2006969820541100033.json、图片生成/文生图/（量贩版）Qwen 2512 Kook真实版极速自动扩写文生图V1_2008588511217192962.json、图片生成/文生图/（量贩版）Qwen Image 2512极速自动扩写文生图 多图多风格_2007703405346689025.json、图片生成/文生图/（量贩版）Qwen Image 2512极速自动扩写文生图V1_2006361347503693825.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Replace`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `UnetLoaderGGUF` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/4 个有
- `ShellAgentPluginOutputText` —— 1/4 个有
- `easy promptLine` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1080 | 1080 - 1200 | 4 | 95% |
| 高度 | 1920 | 1600 - 1920 | 4 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1200，4 个样本，取值集中（一致性 95%）
- 高度 中位数 1920，观测区间 1600 - 1920，4 个样本，取值集中（一致性 92%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
