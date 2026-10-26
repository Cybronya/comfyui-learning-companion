---
name: image_to_image_sampler_vae_18
type: Image To Image
frequency: 9
level: weak
coverage: 0.902778
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/灯光调节器-qwen_image_edit_2511_2011441135843024897.json, 图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099327221906362369.json, 图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099667042474479618.json, 图片生成/图生图/顶级图像编辑模型 Qwen-Image-Edit-2511工作流_2005170734341255169.json, 图片生成/图生图/风格转换qwen2511最新图像编辑换装千问2511追赶nano+全能图片V1(1)_2004060386825519105.json, 图片生成/图生图/（单图推荐）tele style画风迁移，游戏_动漫角色设计_2054939690477858817.json, 图片生成/图生图/👾怪獸-QWEN-EDIT-2511+重打光强化版👾_2014642307299020802.json, 图片生成/文生图/Qwen Edit 2511 图片去水印 全节点注释_2077810588885020674.json, 图片生成/文生图/千问2511单图编辑_2004111023990841345.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_18

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/灯光调节器-qwen_image_edit_2511_2011441135843024897.json、图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099327221906362369.json、图片生成/图生图/灯光调节器-qwen_image_edit_2511_2099667042474479618.json、图片生成/图生图/顶级图像编辑模型 Qwen-Image-Edit-2511工作流_2005170734341255169.json、图片生成/图生图/风格转换qwen2511最新图像编辑换装千问2511追赶nano+全能图片V1(1)_2004060386825519105.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 8/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `UNETLoader` —— 6/9 个有
- `QwenMultiangleLightningNode` —— 4/9 个有
- `Anything Everywhere3` —— 3/9 个有
- `CR Text` —— 3/9 个有
- `RHHiddenNodes` —— 3/9 个有
- `ImageConcatMulti` —— 2/9 个有
- `ImageConcanate` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 9 | 3% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 9 | 72% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，9 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
