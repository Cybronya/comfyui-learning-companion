---
name: unknown_workflow_video_lora_sampler_92
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.500437
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [视频生成/图生视频/2007636774910173185.json, 视频生成/图生视频/1999450215444869122.json, 视频生成/图生视频/1987760541282316290.json, 视频生成/图生视频/1986333463185948673.json, 视频生成/图生视频/1983825079475838977.json, 视频生成/图生视频/1984268065183514625.json, 视频生成/图生视频/1991421095259631618.json, 视频生成/图生视频/1988481476389945345.json, 视频生成/图生视频/1997917830655934465.json, 视频生成/图生视频/1997912298406731777.json, 视频生成/图生视频/2035400286210105346.json, 视频生成/图生视频/2034928021357989889.json, 视频生成/图生视频/1964155751138775041.json, 视频生成/图生视频/1989490434684669953.json, 视频生成/图生视频/1986291016309362690.json, 视频生成/图生视频/1994048317403447297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_92

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2007636774910173185.json、视频生成/图生视频/1999450215444869122.json、视频生成/图生视频/1987760541282316290.json、视频生成/图生视频/1986333463185948673.json、视频生成/图生视频/1983825079475838977.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 15/16 个有
- `AILab_QwenVL` —— 12/16 个有
- `PreviewAny` —— 12/16 个有
- `WanImageToVideo` —— 11/16 个有
- `GetImageRangeFromBatch` —— 7/16 个有
- `FlashVSRNode` —— 4/16 个有
- `PainterI2V` —— 3/16 个有
- `WanFirstLastFrameToVideo` —— 3/16 个有
- `CR SDXL Aspect Ratio` —— 1/16 个有
- `ColorMatch` —— 1/16 个有
- `GetImageSizeAndCount` —— 1/16 个有
- `JWStringConcat` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `RH_Translator` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 69% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 16 | 88% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | lcm | - | 16 | 100% |
| 重绘幅度 | simple | - | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 69%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，16 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，16 个样本，一致性 100%
- 重绘幅度 最常用 simple，16 个样本，一致性 100%
