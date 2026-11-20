---
name: unknown_workflow_video_lora_sampler_804
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.654333
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Bernini视频分段编辑【二创神器】_2072825480406982657.json, 平台全量/bernini人物替换_2062063367837278210.json, 视频生成/图生视频/贝尔尼尼 Bernini 视频编辑工作流V 1.0_2062439280944963586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_804

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Bernini视频分段编辑【二创神器】_2072825480406982657.json、平台全量/bernini人物替换_2062063367837278210.json、视频生成/图生视频/贝尔尼尼 Bernini 视频编辑工作流V 1.0_2062439280944963586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Value` —— 1/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LoadVideoUI` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `VHS_VideoInfoLoaded` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `kkVideoFramesAdvanced` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
