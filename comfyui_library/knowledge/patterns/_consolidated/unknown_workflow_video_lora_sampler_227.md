---
name: unknown_workflow_video_lora_sampler_227
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.645182
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, SamplerCustom, SplitSigmas, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/AI代码侠土豆-Bernini 电商换产品视频编辑_2062397821210423297.json, 平台全量/Bernini 视频换人换背景_2063178699649933314.json, 平台全量/Bernini-视频编辑-字节开源-基于wan2.2_2065440184044445698.json, 平台全量/Bernini视频编辑-v1.0_2070757377581867010.json, 平台全量/Bernini视频编辑-v1_2077664467026014209.json, 平台全量/Character Video Costume Changes人物视频换装_2099665216236773377.json, 平台全量/最新字节开源Bernini+电商换产品+视频编辑_2064723591240966145.json, 平台全量/电商服饰产品展示 万物迁移 换装换衣 模特人物换脸+电商服装展示_2065063988869812225.json, 视频生成/图生视频/Bernini 视频人物替换_2063568114679369730.json, 视频生成/图生视频/电商服饰产品展示 万物迁移 视频换脸换装换衣 模特人物换脸+电商服装展示 Bernini+电商换产品_2064890559977840642.json, 视频生成/图生视频/视频换装换衣+电商服饰产品展示+ 模特人物换脸 电商服装展示  Bernini+电商换产品视频编辑_2064510607130451970.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_227

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/AI代码侠土豆-Bernini 电商换产品视频编辑_2062397821210423297.json、平台全量/Bernini 视频换人换背景_2063178699649933314.json、平台全量/Bernini-视频编辑-字节开源-基于wan2.2_2065440184044445698.json、平台全量/Bernini视频编辑-v1.0_2070757377581867010.json、平台全量/Bernini视频编辑-v1_2077664467026014209.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 10/11 个有
- `ImageResizeKJv2` —— 8/11 个有
- `TTResolutionSelector` —— 8/11 个有
- `Text` —— 8/11 个有
- `easy cleanGpuUsed` —— 8/11 个有
- `easy showAnything` —— 8/11 个有
- `GetNode` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `Int` —— 3/11 个有
- `easy getNode` —— 3/11 个有
- `easy setNode` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `LoadVideo` —— 2/11 个有
- `VAEDecodeTiled` —— 1/11 个有
- `easy mathInt` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
