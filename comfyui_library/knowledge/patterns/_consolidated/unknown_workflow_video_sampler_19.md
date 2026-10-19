---
name: unknown_workflow_video_sampler_19
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.893
common_nodes: [Any To Any, CR Prompt Text, MMAudioFeatureUtilsLoader, MMAudioModelLoader, MMAudioSampler, Qwen3_VQA, VHS_LoadVideo, VHS_SelectFilename, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/MMaudio + Qwen3 VL自动视频配音效_1985682788978438146.json, 音频生成/音频生成/MMaudio + Qwen3 VL视频配音效优化版V1_2043507645843247106.json, 音频生成/音频生成/MMaudio视频配音效（提示词增强）_2054751569878503426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/MMaudio + Qwen3 VL自动视频配音效_1985682788978438146.json、音频生成/音频生成/MMaudio + Qwen3 VL视频配音效优化版V1_2043507645843247106.json、音频生成/音频生成/MMaudio视频配音效（提示词增强）_2054751569878503426.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `Any To Any`
- `CR Prompt Text`
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `MMAudioSampler`
- `Qwen3_VQA`
- `VHS_LoadVideo`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GoogleTranslateTextNode` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `Int` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
