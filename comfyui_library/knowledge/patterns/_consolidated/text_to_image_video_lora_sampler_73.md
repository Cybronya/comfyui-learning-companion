---
name: text_to_image_video_lora_sampler_73
type: Text To Image
frequency: 11
level: moderate
coverage: 0.657364
common_nodes: [AILab_QwenVL, CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, EmptyLatentImage, ImageResizeKJv2, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, RIFE VFI, SaveImage, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy int, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/电商男装_女装+一键产品展示视频+全节点注释_2045844005568651266.json, 视频生成/图生视频/电商产品展示视频-阿浩_2039598671024623618.json, 视频生成/图生视频/电商男装_女装 一键产品展示视频_2035988897074778114.json, 视频生成/图生视频/电商男装_女装 带货_2049669037273124866.json, 视频生成/图生视频/电商男装_女装+一键产品展示视频+全节点注释_2042497387209433090.json, 视频生成/图生视频/电商男装_女装带货视频+一键产品展示视频_2063940352813395969.json, 视频生成/图生视频/电商男装_女装带货视频+一键产品展示视频_2073243113539330049.json, 视频生成/图生视频/电商男装_女装带货视频+一键产品展示视频_2116694628215910402.json, 视频生成/图生视频/电商男装女装穿搭带货走动视频【图生视频】_2064728574678097922.json, 视频生成/文生视频/电商男女装带货视频 一键产品展示换背景运镜处理工具_2112994809882435586.json, 视频生成/文生视频/电商男装_女装带货视频+一键产品展示视频_2054126270811787265.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_73

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/电商男装_女装+一键产品展示视频+全节点注释_2045844005568651266.json、视频生成/图生视频/电商产品展示视频-阿浩_2039598671024623618.json、视频生成/图生视频/电商男装_女装 一键产品展示视频_2035988897074778114.json、视频生成/图生视频/电商男装_女装 带货_2049669037273124866.json、视频生成/图生视频/电商男装_女装+一键产品展示视频+全节点注释_2042497387209433090.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 11 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy int`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 3/11 个有
- `JjkText` —— 1/11 个有
- `TT_img_enc` —— 1/11 个有
- `solarL_SaveImagesToZip` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 82% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 11 | 73% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | 1 | 1 - 1 | 9 | 100% |
| 重绘幅度 | euler_ancestral | - | 11 | 82% |
| 宽度 | 1168 | 80 - 1168 | 11 | 71% |
| 高度 | 1536 | 80 - 1536 | 11 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 82%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，11 个样本
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，11 个样本，一致性 82%
- 宽度 中位数 1168，观测区间 80 - 1168，11 个样本
- 高度 中位数 1536，观测区间 80 - 1536，11 个样本
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
