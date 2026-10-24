---
name: text_to_image_lora_sampler_clip_570
type: Text To Image
frequency: 2
level: weak
coverage: 0.887
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyImage, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax导演台自动提示词版｜一键自动生成不用写词，出片零门槛_2099492125976125442.json, 图片生成/图生图/俯视图拆九宫格平视分镜横板｜全能图像G低价渠道，图生图分镜省时省力_2100441395935924225.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_570

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/MiniMax导演台自动提示词版｜一键自动生成不用写词，出片零门槛_2099492125976125442.json、图片生成/图生图/俯视图拆九宫格平视分镜横板｜全能图像G低价渠道，图生图分镜省时省力_2100441395935924225.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GuHaiAutoImageSplit` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `MultiTextConcatenate` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `RH_Utils` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `Text` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
