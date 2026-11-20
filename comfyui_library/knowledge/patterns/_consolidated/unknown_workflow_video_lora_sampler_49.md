---
name: unknown_workflow_video_lora_sampler_49
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.734227
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text Concatenate, Florence2ModelLoader, Florence2Run, INTConstant, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoTeaCacheKJ, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/WAN21特图生视频效合集_1930497096028426242.json, 视频生成/图生视频/Wan图生视频_运镜_1931553417045409794.json, 视频生成/图生视频/wan2.1 运镜lora_1927308974876692481.json, 视频生成/图生视频/一键电影运镜视频_1929861352612073473.json, 视频生成/图生视频/图片生成运镜视频（电影级）123_1929395097194938370.json, 视频生成/图生视频/图片生成运镜视频（电影级）_2043240803773980674.json, 视频生成/图生视频/图片生成运镜视频（电影级）_2043244111414697986.json, 视频生成/图生视频/图片生成运镜视频（电影运镜）_1929565877887471617.json, 视频生成/图生视频/图片运镜_2007615510288011266.json, 视频生成/图生视频/图生视频--效果超出想象---WAN21特图生视频效合集_2048597647006633986.json, 视频生成/图生视频/图生视频--效果超出想象---WAN21特图生视频效合集_2048657356048834561.json, 视频生成/图生视频/图生视频丨运镜视频合集（11款）_1978647980314136577.json, 视频生成/图生视频/电影1图片转运镜视频_1929869489117237249.json, 视频生成/图生视频/电影级别 运镜 图生视频 合集_1996871652937977858.json, 视频生成/图生视频/电影级别图片生成运镜视频_1929847163700854786.json, 视频生成/图生视频/电影级别运镜图生视频_1930122679813095426.json, 视频生成/图生视频/电影级别运镜图生视频合集_1930199609451384834.json, 视频生成/图生视频/电影级别运镜图生视频合集_1937550595018375170.json, 视频生成/图生视频/电影级别运镜图生视频合集_1980239592316186626.json, 视频生成/图生视频/电影级别运镜图生视频合集_1989638202606669825.json, 视频生成/图生视频/龙明wan2.1 运镜lora_1934983961166684161.json, 视频生成/文生视频/图片生成运镜视频（电影级）123_1951765085700214786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/WAN21特图生视频效合集_1930497096028426242.json、视频生成/图生视频/Wan图生视频_运镜_1931553417045409794.json、视频生成/图生视频/wan2.1 运镜lora_1927308974876692481.json、视频生成/图生视频/一键电影运镜视频_1929861352612073473.json、视频生成/图生视频/图片生成运镜视频（电影级）123_1929395097194938370.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text Concatenate`
- `Florence2ModelLoader`
- `Florence2Run`
- `INTConstant`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 19/22 个有
- `PrimitiveString` —— 19/22 个有
- `VHS_LoadVideo` —— 19/22 个有
- `CR Prompt Text` —— 13/22 个有
- `ShowText|pysssss` —— 10/22 个有
- `easy getNode` —— 9/22 个有
- `easy setNode` —— 9/22 个有
- `CR Text` —— 6/22 个有
- `Primitive integer [Crystools]` —— 1/22 个有
- `easy anythingIndexSwitch` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 22 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 22 | 100% |
| 采样算法 | uni_pc | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
