---
name: unknown_workflow_video_lora_sampler_482
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.70925
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SplitSigmas, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Bernini 视频人物替换_2063568114679369730.json, 视频生成/图生视频/电商服饰产品展示 万物迁移 视频换脸换装换衣 模特人物换脸+电商服装展示 Bernini+电商换产品_2064890559977840642.json, 视频生成/图生视频/视频换装换衣+电商服饰产品展示+ 模特人物换脸 电商服装展示  Bernini+电商换产品视频编辑_2064510607130451970.json, 视频生成/图生视频/贝尔尼尼 Bernini 视频编辑工作流V 1.0_2062439280944963586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_482

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Bernini 视频人物替换_2063568114679369730.json、视频生成/图生视频/电商服饰产品展示 万物迁移 视频换脸换装换衣 模特人物换脸+电商服装展示 Bernini+电商换产品_2064890559977840642.json、视频生成/图生视频/视频换装换衣+电商服饰产品展示+ 模特人物换脸 电商服装展示  Bernini+电商换产品视频编辑_2064510607130451970.json、视频生成/图生视频/贝尔尼尼 Bernini 视频编辑工作流V 1.0_2062439280944963586.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 3/4 个有
- `TTResolutionSelector` —— 3/4 个有
- `Text` —— 3/4 个有
- `VAEDecode` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `BatchImagesNode` —— 1/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `Int` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
