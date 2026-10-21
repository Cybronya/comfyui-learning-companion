---
name: unknown_workflow_video_lora_sampler_523
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91175
common_nodes: [CreateCFGScheduleFloatList, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1968572252335812609.json, 视频生成/图生视频/2071155047878193153.json, 视频生成/图生视频/1979152204013670402.json, 视频生成/文生视频/Wan2.2-14B 图生视频360度后空翻123_2001304184546881538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_523

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1968572252335812609.json、视频生成/图生视频/2071155047878193153.json、视频生成/图生视频/1979152204013670402.json、视频生成/文生视频/Wan2.2-14B 图生视频360度后空翻123_2001304184546881538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `Bjornulf_ShowInt` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `ShowText` —— 2/4 个有
- `DF_Int_to_Float` —— 1/4 个有
- `DF_Integer` —— 1/4 个有
- `DF_Text_Box` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
