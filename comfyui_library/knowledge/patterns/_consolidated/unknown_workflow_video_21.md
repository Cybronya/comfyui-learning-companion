---
name: unknown_workflow_video_21
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8965
common_nodes: [Any To Any, CR Prompt Text, GetVideoComponents, HunyuanVideoFoley, LoadVideo, Qwen3_VQA, VHS_SelectFilename, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/【橘子AI】视频音效生成  Foley-Qwen 反推_1988964595618418689.json, 音频生成/音频生成/混元Foley+Qwen3 VL自动视频音效优化版V1_2043505374543749121.json, 音频生成/音频生成/混元Foley+Qwen3 VL自动视频音效工作流V1_1985680738127360002.json, 音频生成/音频生成/混元Foley视频自动配音效（提示增强）_2054739137890144258.json, 音频生成/音频生成/视频添加音效 混元Foley_2092948660618354689.json, 音频生成/音频生成/视频音效生成  Foley-Qwen_1988180765982769154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_21

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/【橘子AI】视频音效生成  Foley-Qwen 反推_1988964595618418689.json、音频生成/音频生成/混元Foley+Qwen3 VL自动视频音效优化版V1_2043505374543749121.json、音频生成/音频生成/混元Foley+Qwen3 VL自动视频音效工作流V1_1985680738127360002.json、音频生成/音频生成/混元Foley视频自动配音效（提示增强）_2054739137890144258.json、音频生成/音频生成/视频添加音效 混元Foley_2092948660618354689.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `Any To Any`
- `CR Prompt Text`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `LoadVideo`
- `Qwen3_VQA`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 5/6 个有
- `MultiplePathsInput` —— 2/6 个有
- `Int` —— 1/6 个有
- `SaveLatent` —— 1/6 个有
- `VAEEncode` —— 1/6 个有
- `VAELoader` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有
- `easy float` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
