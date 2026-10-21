---
name: unknown_workflow_video_lora_sampler_167
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.773364
common_nodes: [CreateCFGScheduleFloatList, JWInteger, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [ImageFromBatch+, LayerColor: Brightness & Contrast, MathExpression|pysssss, easy anythingIndexSwitch, easy cleanGpuUsed]
members: [视频生成/图生视频/1965347349298036737.json, 视频生成/图生视频/1950542819607891970.json, 视频生成/图生视频/2013815675508232194.json, 视频生成/文生视频/1959814515066089473.json, 视频生成/文生视频/1959882410156568578.json, 视频生成/文生视频/1958719842708832257.json, 视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json, 视频生成/文生视频/Wan2.2-14B 图生视频-123_2001306225730088961.json, 视频生成/文生视频/1950428124720881665.json, 视频生成/文生视频/1957626244445696001.json, 视频生成/文生视频/1962018949422628865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_167

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1965347349298036737.json、视频生成/图生视频/1950542819607891970.json、视频生成/图生视频/2013815675508232194.json、视频生成/文生视频/1959814515066089473.json、视频生成/文生视频/1959882410156568578.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 11 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `JWInteger`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Prompter` —— 10/11 个有
- `TextCombinerTwo` —— 10/11 个有
- `easy showAnything` —— 10/11 个有
- `ImpactSwitch` —— 9/11 个有
- `Int` —— 9/11 个有
- `easy anythingIndexSwitch` —— 9/11 个有
- `WanVideoBlockSwap` —— 7/11 个有
- `WanVideoEmptyEmbeds` —— 7/11 个有
- `easy cleanGpuUsed` —— 7/11 个有
- `WanVideoSetBlockSwap` —— 6/11 个有
- `ImageFromBatch+` —— 5/11 个有
- `LayerColor: Brightness & Contrast` —— 5/11 个有
- `LoadImage` —— 5/11 个有
- `WanVideoImageToVideoEncode` —— 4/11 个有
- `ImageResize+` —— 3/11 个有
- `RH_Captioner` —— 3/11 个有
- `RH_Translator` —— 3/11 个有
- `PreviewImage` —— 2/11 个有
- `Anything Everywhere` —— 1/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `LoadImagesFromURL` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、LayerColor: Brightness & Contrast、MathExpression|pysssss、easy anythingIndexSwitch、easy cleanGpuUsed
