---
name: unknown_workflow_video_lora_sampler_142
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.789167
common_nodes: [CreateCFGScheduleFloatList, JWInteger, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-14B 图生视频-480P_1965347349298036737.json, 视频生成/图生视频/Wan2.2-14B 图生视频-极速版_1957628788819554305.json, 视频生成/图生视频/Wan2.2-14B 图生视频_1950542819607891970.json, 视频生成/图生视频/Wan2.2-14B+图生视频-极速24G可用_2013815675508232194.json, 视频生成/文生视频/AI-Wan2.2-14B 文生视频-极速版_1959882410156568578.json, 视频生成/文生视频/AI站-Wan2.2-14B+文生视频-极速版_1958719842708832257.json, 视频生成/文生视频/CN-Wan2.2-14B 文生视频-极速版_1959814515066089473.json, 视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json, 视频生成/文生视频/Wan2.2-14B 图生视频-123_2001306225730088961.json, 视频生成/文生视频/Wan2.2-14B 文生视频-极速版_1950428124720881665.json, 视频生成/文生视频/Wan2.2-14B 文生视频-极速版_1957626244445696001.json, 视频生成/文生视频/文生视频-Wan2.2（优化版）_1962018949422628865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_142

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-14B 图生视频-480P_1965347349298036737.json、视频生成/图生视频/Wan2.2-14B 图生视频-极速版_1957628788819554305.json、视频生成/图生视频/Wan2.2-14B 图生视频_1950542819607891970.json、视频生成/图生视频/Wan2.2-14B+图生视频-极速24G可用_2013815675508232194.json、视频生成/文生视频/AI-Wan2.2-14B 文生视频-极速版_1959882410156568578.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 12 个 workflow 都包含：
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
- `RH_Prompter` —— 11/12 个有
- `TextCombinerTwo` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `ImpactSwitch` —— 10/12 个有
- `Int` —— 10/12 个有
- `easy anythingIndexSwitch` —— 10/12 个有
- `WanVideoBlockSwap` —— 8/12 个有
- `WanVideoEmptyEmbeds` —— 7/12 个有
- `easy cleanGpuUsed` —— 7/12 个有
- `LoadImage` —— 6/12 个有
- `WanVideoSetBlockSwap` —— 6/12 个有
- `ImageFromBatch+` —— 5/12 个有
- `LayerColor: Brightness & Contrast` —— 5/12 个有
- `WanVideoImageToVideoEncode` —— 5/12 个有
- `ImageResize+` —— 4/12 个有
- `RH_Captioner` —— 4/12 个有
- `RH_Translator` —— 4/12 个有
- `PreviewImage` —— 3/12 个有
- `Anything Everywhere` —— 1/12 个有
- `CR Text Concatenate` —— 1/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `LoadImagesFromURL` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
