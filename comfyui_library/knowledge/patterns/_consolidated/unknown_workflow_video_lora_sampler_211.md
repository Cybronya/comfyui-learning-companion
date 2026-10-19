---
name: unknown_workflow_video_lora_sampler_211
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.875556
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, DiffusionModelLoaderKJ, ImageBatchExtendWithOverlap, Int, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SimpleMath+, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy forLoopEnd, easy forLoopStart, easy promptLine]
problems: []
missing: []
members: [视频生成/图生视频/2005541494670983170.json, 视频生成/图生视频/2011030476026286081.json, 视频生成/图生视频/2010957164097052674.json, 视频生成/图生视频/2035643056212414465.json, 视频生成/图生视频/2011772862205534209.json, 视频生成/图生视频/2011765719033188353.json, 视频生成/图生视频/2011775856401715201.json, 视频生成/图生视频/2010976996687351810.json, 视频生成/图生视频/2012053341018263553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_211

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2005541494670983170.json、视频生成/图生视频/2011030476026286081.json、视频生成/图生视频/2010957164097052674.json、视频生成/图生视频/2035643056212414465.json、视频生成/图生视频/2011772862205534209.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DiffusionModelLoaderKJ`
- `ImageBatchExtendWithOverlap`
- `Int`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SimpleMath+`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `> Text Replace` —— 4/9 个有
- `CR Prompt Text` —— 4/9 个有
- `CR Text Concatenate` —— 4/9 个有
- `ProcessString` —— 4/9 个有
- `Qwen3_VQA` —— 4/9 个有
- `TextPreview` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `SomethingToString` —— 3/9 个有
- `Split String` —— 3/9 个有
- `DuckHideNode` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `TT_img_enc` —— 2/9 个有
- `TT_img_enc_v2` —— 2/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 56% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 9 | 100% |
| 采样算法 | 3.5 | 1 - 3.5 | 9 | 48% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3.5，观测区间 1 - 3.5，9 个样本，取值分散，一致性仅 48%
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
